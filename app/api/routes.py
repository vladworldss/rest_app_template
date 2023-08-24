from fastapi import APIRouter
from starlette.responses import PlainTextResponse

from app.api.urls import HEALTH_PATH

app_router = APIRouter()


@app_router.get(HEALTH_PATH, response_class=PlainTextResponse)
async def health() -> str:
    return 'Healthy'
