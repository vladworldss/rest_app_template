import asyncio

import asyncpg
import pytest
import pytest_asyncio

from httpx import AsyncClient

from app.settings import get_settings

CONFIG = get_settings()


@pytest.fixture(scope="session")
def event_loop():
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


@pytest_asyncio.fixture(scope="session")
async def async_app_client():
    async with AsyncClient(base_url='http://app:8000') as client:
        yield client


@pytest_asyncio.fixture(scope='session')
async def pg_connection():
    conn: asyncpg.Connection = await asyncpg.connect(CONFIG.database.dsn)
    yield conn
    await conn.close()


@pytest_asyncio.fixture
async def clear_db(pg_connection):
    await pg_connection.execute('truncate emails.email;')
    yield
