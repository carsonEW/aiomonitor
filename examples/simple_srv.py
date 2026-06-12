import asyncio

import aiomonitor
from aiohttp import web

# Simple handler that returns response after 100s
async def simple(request):
    print('Start sleeping')
    await asyncio.sleep(100)
    return web.Response(text="Simple answer")

loop = asyncio.get_event_loop()
# create application and register route
app = web.Application()
app.router.add_get('/simple', simple)

# it is possible to pass a dictionary with local variables
# to the python console environment
host, port = "localhost", 8090
locals_ = {"port": port, "host": host}
# init monitor just before run_app
with aiomonitor.start_monitor(loop=loop, locals=locals_):
    # run application with built-in aiohttp run_app function
    web.run_app(app, port=port, host=host, loop=loop)