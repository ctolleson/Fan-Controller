import asyncio,json,sys
from pathlib import Path
from kicad_mcp.server import build_server

async def main():
    server=build_server('full')
    async def call(name,args):
        result=await server.call_tool(name,args)
        s=json.dumps(result,default=str)
        print(name,s[:18000],flush=True)
        return result
    await call('kicad_set_project',{'project_dir':'/Users/ctolleson/Documents/Claude/PWM_Fan_Controller/KiCad/fancontroller'})
    for c in json.loads(Path(sys.argv[1]).read_text()):
        await call(c['tool'],c.get('args',{}))

asyncio.run(main())
