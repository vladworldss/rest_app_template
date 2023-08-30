import json

from uuid import UUID

import pytest

CREATE_EMAIL = '/email/create'


@pytest.mark.asyncio
async def test_create_email_successful(pg_connection, async_app_client):
    body = {
        "smtp_address_from": "test_from@123mail.com",
        "smtp_address_to": "test_to@123mail.com",
        "subject": "test_title",
        "body": "some body text",
    }
    response = await async_app_client.post(CREATE_EMAIL, data=json.dumps(body))
    assert response.status_code == 200
    assert UUID(response.json())
