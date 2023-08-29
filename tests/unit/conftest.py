from asyncio import Future
from contextlib import asynccontextmanager
from unittest.mock import MagicMock, patch

import pytest

from app.db.repositories.email.repo import EmailRepository
from app.settings import ServerSettings


@pytest.fixture
def async_result():
    def _foo(value) -> Future:
        future: Future = Future()
        future.set_result(value)

        return future

    return _foo


@pytest.fixture(autouse=True)
def settings():
    server_settings = ServerSettings(
        host='127.0.0.1',
        port=7799,
        debug=True,
    )

    app_settings = MagicMock(server=server_settings, database=MagicMock())

    with patch('app.settings.get_settings', lambda *args, **kw: app_settings):
        yield app_settings


@pytest.fixture
def db_connection():
    class Pool:
        @asynccontextmanager
        async def acquire(self):
            yield self

        @asynccontextmanager
        async def transaction(self):
            yield self

        async def executemany(self, *args, **kwargs):
            pass

        async def set_type_codec(self, *args, **kwargs):
            pass

        async def execute(self, *args, **kwargs):
            pass

        async def fetch(self, *args, **kwargs):
            pass

        async def fetchval(self, *args, **kwargs):
            pass

        async def fetchrow(self, *args, **kwargs):
            pass

    yield Pool()


@pytest.fixture
def email_repo(db_connection, settings):
    yield EmailRepository(db_pool=db_connection)
