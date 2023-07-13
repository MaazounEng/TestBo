import os

from aiohttp import web

routes = web.RouteTableDef()

@routes.get("/")
async def main(request):
    return web.Response(status=200, text="Hello world!")


if __name__ == "__main__":
    app = web.Application()
    app.add_routes(routes)
    port = os.environ.get("PORT")
    if port is not None:
        port = int(port)
    else:
        port = 8080  # Default port to 8080 if PORT environment variable is not set

    web.run_app(app, host="localhost", port=port)
