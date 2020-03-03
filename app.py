# import logging; logging.basicConfig(level=logging.INFO)
#
# import asyncio, os, json, time
# from datetime import datetime
#
# from aiohttp import web
#
#
# def index(request):
#     return web.Response(body=b'<h1>Awesome</h1>')
#
# async def init(loop):
#     app = web.Application(loop=loop)
#     app.router.add_route('GET','/',index)
#     app_runner = web.AppRunner(app)
#     await app_runner.setup()
#     srv = await loop.create_server(app_runner.server,'127.0.0.1',9000)
#     logging.info('server started at http://127.0.0.1:9000...')
#     return  srv
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(init(loop))
# loop.run_forever()

import logging; logging.basicConfig(level=logging.INFO)

import asyncio, os, json, time
from datetime import datetime

from aiohttp import web, web_runner


routes = web.RouteTableDef()


@routes.get('/')
def index(request):
    return web.Response(body=b'<h1>Awesome App</h1>', content_type='text/html')


def init():
    app = web.Application()
    app.add_routes([web.get('/', index)])
    logging.info('server started at http://127.0.0.1:9257...')
    web.run_app(app, host='127.0.0.1', port=9527)


init()