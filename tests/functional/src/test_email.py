import json

from uuid import UUID

import pytest

from app.api.routes import CREATE_EMAIL, GET_EMAIL


@pytest.mark.asyncio
async def test_create_email_successful(clear_db, pg_connection, async_app_client):
    body = {
        "smtp_address_from": "test_from@123mail.com",
        "smtp_address_to": "test_to@123mail.com",
        "subject": "test_title",
        "body": "some body text",
    }
    response = await async_app_client.post(CREATE_EMAIL, data=json.dumps(body))
    assert response.status_code == 200
    assert UUID(response.json())


@pytest.mark.asyncio
async def test_get_email_successful(clear_db, pg_connection, async_app_client):
    body = {
        "smtp_address_from": "test_from@123mail.com",
        "smtp_address_to": "test_to@123mail.com",
        "subject": "test_title",
        "body": "some body text",
    }
    response = await async_app_client.post(CREATE_EMAIL, data=json.dumps(body))
    assert response.status_code == 200
    email_id = response.json()
    assert email_id

    response = await async_app_client.get(GET_EMAIL.format(email_id=email_id))
    assert response.status_code == 200
    email_created = response.json()
    assert email_created

    for k, v in body.items():
        assert v == email_created[k]
