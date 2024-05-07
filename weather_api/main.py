from fastapi import FastAPI

from weather_api.routers import (
    root,
    cities,
)


def create_app() -> FastAPI:
    app = FastAPI(
        title="WeatherAPI",
    )

    app.include_router(root.router)
    app.include_router(cities.router)

    return app
