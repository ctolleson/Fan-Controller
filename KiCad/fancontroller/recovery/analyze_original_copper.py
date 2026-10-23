import json,re
from pathlib import Path
from collections import defaultdict
from gerbonara import GerberFile,ExcellonFile
from shapely.geometry import Point,Polygon,LineString,box
from shapely.ops import unary_union
from shapely.affinity import rotate

root=Path('/Users/ctolleson/Documents/Claude/PWM_Fan_Controller')
def geom(p):
    t=type(p).__name__
    if t=='Circle':return Point(p.x,p.y).buffer(p.r,resolution=32)
    if t=='Line':return LineString([(p.x1,p.y1),(p.x2,p.y2)]).buffer(p.width/2,resolution=32)
    if t=='Rectangle':return rotate(box(p.x-p.w/2,p.y-p.h/2,p.x+p.w/2,p.y+p.h/2),p.rotation*180/3.141592653589793,origin=(p.x,p.y))
    if t=='ArcPoly':
        assert not any(p.arc_centers)
        return Polygon(p.outline).buffer(0)
    raise ValueError(t)
polys=[];shapes={};src={}
for side in ['F','B']:
    g=GerberFile.open(root/f'Gerber/fancontroller-{side}.Cu.gbr')
    src[side]=g
    u=unary_union([geom(p) for o in g.objects for p in o.to_primitives()])
    ps=list(u.geoms) if hasattr(u,'geoms') else [u]
    for p in ps:
        shapes[len(polys)]=side;polys.append(p)
parent=list(range(len(polys)))
def find(i):
    if parent[i]!=i:parent[i]=find(parent[i])
    return parent[i]
def union(a,b):parent[find(a)]=find(b)
dr=ExcellonFile.open(root/'Gerber/fancontroller-PTH.drl')
for hole in dr.objects:
    hole.convert_to('mm')
    point=Point(hole.x,hole.y)
    ids=[i for i,p in enumerate(polys) if p.distance(point)<.00001]
    for i in ids[1:]:union(ids[0],i)
text=(root/'Gerber/fancontroller-F.Cu.gbr').read_text()
pads={}
for m in re.finditer(r'TO.P,([^,*]+),([^,*]+)\*.*?X(-?\d+)Y(-?\d+)D03',text,re.S):
    ref,pin,x,y=m.groups();pads[ref+'.'+pin]=(int(x)/1e6,int(y)/1e6)
groups=defaultdict(list)
for name,xy in pads.items():
    ids=[i for i,p in enumerate(polys) if shapes[i]=='F' and p.distance(Point(*xy))<.00001]
    assert len(ids)==1,(name,ids)
    groups[find(ids[0])].append(name)
for key,ns in sorted(groups.items(),key=lambda kv:(-len(kv[1]),kv[0])):print(key,','.join(sorted(ns)))
result={'groups':dict(groups),'pad_xy':pads,'tracks':[],'vias':[]}
for side,g in src.items():
    for o in g.objects:
        if type(o).__name__=='Line':
            point=Point((o.x1+o.x2)/2,(o.y1+o.y2)/2)
            ids=[i for i,p in enumerate(polys) if shapes[i]==side and p.distance(point)<.00001]
            assert len(ids)==1,ids
            result['tracks'].append({'x1_mm':o.x1,'y1_mm':-o.y1,'x2_mm':o.x2,'y2_mm':-o.y2,'width_mm':o.aperture.diameter,'layer':side+'_Cu','group':find(ids[0])})
for h in dr.objects:
    drill=h.tool.unit.convert_to('mm',h.tool.diameter)
    if drill>.7:continue
    ids=[i for i,p in enumerate(polys) if p.distance(Point(h.x,h.y))<.00001]
    flashes=[o for o in src['F'].objects if type(o).__name__=='Flash' and abs(o.x-h.x)<.02 and abs(o.y-h.y)<.02]
    result['vias'].append({'x_mm':h.x,'y_mm':-h.y,'drill_mm':drill,'diameter_mm':max(o.aperture.diameter for o in flashes),'group':find(ids[0])})
Path('/private/tmp/fan-copper-connectivity.json').write_text(json.dumps(result,indent=2))
print('counts',len(result['tracks']),len(result['vias']),len(polys),len(groups))
