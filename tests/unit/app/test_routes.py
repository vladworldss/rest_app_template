from app.api.routes import CREATE_EMAIL, HEALTH_PATH
from tests.unit.testdata import STATIC_UUID

from .testdata import CREATE_EMAIL_REQUEST_BODY


def test_health(client):
    resp = client.get(HEALTH_PATH)
    assert resp.status_code == 200
    assert resp.text == 'Healthy'


def test_create_new_email(client, override_email_repo_dependency):
    resp = client.post(
        CREATE_EMAIL,
        json=CREATE_EMAIL_REQUEST_BODY,
    )
    assert resp.status_code == 200
    assert resp.json() == str(STATIC_UUID)
