from unittest.mock import patch

import pytest

from fastapi import FastAPI
from fastapi.testclient import TestClient

from app.api.routes import app_router
from app.dependencies import get_email_repo
from tests.unit.testdata import STATIC_UUID


@pytest.fixture
def app(settings) -> FastAPI:
    with patch('app.dependencies.get_settings', lambda *args, **kw: settings):
        _app = FastAPI()
        _app.state.config = settings
        _app.include_router(app_router)

        yield _app


@pytest.fixture
def client(app) -> TestClient:
    _client = TestClient(app)

    yield _client


@pytest.fixture
def override_email_repo_dependency(when2, app, email_repo, async_result):
    async def _foo():
        when2(email_repo.create_email, ...).thenReturn(async_result(STATIC_UUID))
        return email_repo

    app.dependency_overrides[get_email_repo] = _foo
    yield


@pytest.fixture
def override_email_repo_empty_mock(when2, async_result, app):
    async def _foo():
        return

    app.dependency_overrides[get_email_repo] = _foo
    yield
