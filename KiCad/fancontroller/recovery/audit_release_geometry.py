"""Read-only geometry audit; never writes KiCad source files.

Run with the gerbonara/Shapely recovery venv. sexpdata is available in the
KiCad MCP venv; supply its site-packages directory through PYTHONPATH.
"""
import json
import math
import sys
from pathlib import Path

import sexpdata
from shapely import affinity
from shapely.geometry import LineString, Point, Polygon, box
from shapely.ops import polygonize, unary_union


def children(node, key):
    return [v for v in node[1:] if isinstance(v, list) and v and str(v[0]) == key]


def child(node, key):
    return next(iter(children(node, key)), None)


project = Path(__file__).resolve().parents[1]
root = sexpdata.loads((project / "fancontroller.kicad_pcb").read_text())
edge_points = []
for line in children(root, "gr_line"):
    if child(line, "layer")[1] == "Edge.Cuts":
        edge_points.extend([child(line, "start")[1:3], child(line, "end")[1:3]])
board = box(min(p[0] for p in edge_points), min(p[1] for p in edge_points),
            max(p[0] for p in edge_points), max(p[1] for p in edge_points))
courtyards = {}
missing = []
silk_text = []
for fp in children(root, "footprint"):
    ref = next(v[2] for v in children(fp, "property") if v[1] == "Reference")
    at = child(fp, "at")
    x, y = at[1:3]
    angle = at[3] if len(at) > 3 else 0
    lines, shapes = [], []
    for item in fp[1:]:
        if not isinstance(item, list) or not item:
            continue
        layer = child(item, "layer")
        if not layer or layer[1] != "F.CrtYd":
            continue
        kind = str(item[0])
        if kind == "fp_line":
            lines.append(LineString([child(item, "start")[1:3], child(item, "end")[1:3]]))
        elif kind == "fp_rect":
            a, b = child(item, "start")[1:3], child(item, "end")[1:3]
            shapes.append(box(min(a[0], b[0]), min(a[1], b[1]), max(a[0], b[0]), max(a[1], b[1])))
        elif kind == "fp_circle":
            c, e = child(item, "center")[1:3], child(item, "end")[1:3]
            shapes.append(Point(c).buffer(math.dist(c, e), quad_segs=128))
        else:
            raise ValueError(f"Unsupported courtyard primitive {kind}: {ref}")
    shapes.extend(polygonize(lines))
    if not shapes:
        missing.append(ref)
        continue
    shape = unary_union(shapes)
    courtyards[ref] = affinity.translate(affinity.rotate(shape, -angle, origin=(0, 0)), x, y)

overlaps = []
for index, (a, shape_a) in enumerate(courtyards.items()):
    for b, shape_b in list(courtyards.items())[index + 1:]:
        area = shape_a.intersection(shape_b).area
        if area > 1e-8:
            overlaps.append({"refs": [a, b], "area_mm2": area})
outside = {ref: shape.difference(board).area for ref, shape in courtyards.items()
           if shape.difference(board).area > 1e-8}
review_pairs = ["C2/IC2", "C2/J1", "C3/IC3", "C4/H4", "C5/REG1", "IC1/J2", "IC3/P1", "J1/J2"]
report = {
    "method": "Read-only project footprint courtyard polygons, transformed using actual rotation and origin; board outline is rectangular.",
    "board_bounds_mm": list(board.bounds),
    "courtyards_checked": len(courtyards),
    "missing_courtyards": missing,
    "overlapping_courtyards": overlaps,
    "courtyard_area_outside_board_mm2": outside,
    "flagged_pair_courtyard_gap_mm": {
        pair: round(courtyards[pair.split('/')[0]].distance(courtyards[pair.split('/')[1]]), 6)
        for pair in review_pairs if all(r in courtyards for r in pair.split('/'))
    },
    "limits": "Checks library courtyard geometry, not actual purchased connector bodies, mating cables, screw heads, or 3D component models. Does not waive or change MCP gate findings.",
}
destination = Path(sys.argv[1])
destination.write_text(json.dumps(report, indent=2) + "\n")
print(json.dumps(report, indent=2))
