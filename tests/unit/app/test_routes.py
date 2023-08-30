import pytest

from app.api.routes import CREATE_EMAIL, HEALTH_PATH
from tests.unit.testdata import STATIC_UUID

from .testdata import (
    CREATE_EMAIL_REQUEST_BODY,
    INVALID_ATTR_CREATE_EMAIL_REQUEST_BODY,
    NOT_REQUIRED_ATTR_CREATE_EMAIL_REQUEST_BODY,
)


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


@pytest.mark.parametrize(
    'request_body, exp_resp_status, descr',
    [
        (
            NOT_REQUIRED_ATTR_CREATE_EMAIL_REQUEST_BODY,
            422,
            [{'loc': ['body', 'subject'], 'msg': 'field required', 'type': 'value_error.missing'}],
        ),
        (
            INVALID_ATTR_CREATE_EMAIL_REQUEST_BODY,
            422,
            [{'loc': ['body', 'subject'], 'msg': 'str type expected', 'type': 'type_error.str'}],
        ),
    ],
)
def test_create_new_email_invalid_request(client, override_email_repo_empty_mock, request_body, exp_resp_status, descr):
    resp = client.post(
        CREATE_EMAIL,
        json=request_body,
    )
    assert resp.status_code == exp_resp_status
    assert resp.json()['detail'] == descr
