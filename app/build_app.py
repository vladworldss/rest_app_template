import asyncio

from fastapi import FastAPI

from app.api.routes import app_router
from app.dependencies import get_db_pool

from .settings import Settings, get_settings


def build_app(config: Settings) -> FastAPI:
    app = FastAPI(
        debug=config.server.debug,
        version="1.0.0",
        title="Test app for functional testing",
    )
    config = get_settings()

    app.include_router(app_router)

    app.state.config = config

    @app.on_event('startup')
    async def perform_startup() -> None:
        db_pool = await get_db_pool()

        async with db_pool.acquire() as conn:
            for i in range(10):
                try:
                    await conn.execute('SELECT 1')
                    return None
                except Exception:
                    await asyncio.sleep(1)

            raise Exception(f'Could not connect to {config.database.masked_dsn}')

    @app.on_event('shutdown')
    async def perform_graceful_shutdown() -> None:
        await get_db_pool().close()

    return app
