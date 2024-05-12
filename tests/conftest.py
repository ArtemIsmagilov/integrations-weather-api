import pytest
from fastapi.testclient import TestClient

from weather_api.main import create_app
from weather_api.cached_app.caching import pool


@pytest.fixture()
def app():
    app = create_app()
    yield app


@pytest.fixture()
def client(app):
    return TestClient(app)


@pytest.fixture()
def mock_pool():
    yield pool
