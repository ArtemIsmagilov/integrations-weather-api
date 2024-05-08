from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from weather_api.routers import (
    root,
    cities,
    web,
)


def create_app() -> FastAPI:
    app = FastAPI(
        title="Integrations WeatherAPI",
    )

    app.mount(
        "/static",
        StaticFiles(directory="./weather_api/web_app/static"),
        name="static",
    )

    app.include_router(root.router)
    app.include_router(cities.router)
    app.include_router(web.router)

    return app
