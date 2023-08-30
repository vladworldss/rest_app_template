import pytest

from app.api.routes import HEALTH_PATH


@pytest.mark.asyncio
async def test_ping_ok(async_app_client):
    response = await async_app_client.get(HEALTH_PATH)
    assert response.status_code == 200
    assert response.content == b'Healthy'
