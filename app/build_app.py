from fastapi import FastAPI
from .settings import Settings

from app.api.routes import app_router


def build_app(config: Settings) -> FastAPI:
    app = FastAPI(
        debug=config.server.debug,
        version="1.0.0",
        title="Test app for functional testing",
    )

    app.include_router(app_router)

    return app
