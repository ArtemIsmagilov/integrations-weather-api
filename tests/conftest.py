import asyncio

import pytest
from fastapi.testclient import TestClient

from weather_api.main import create_app
from weather_api.sql_app import init_db
from weather_api.cached_app.caching import pool


@pytest.fixture()
def app():
    app = create_app()
    asyncio.run(init_db.main())
    yield app


@pytest.fixture()
def client(app):
    return TestClient(app)


@pytest.fixture()
def mock_pool():
    yield pool
