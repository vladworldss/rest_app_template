from app.api.models import CreateEmailRequest
from tests.unit.testdata import EMAIL_DATA

CREATE_EMAIL_REQUEST_BODY = CreateEmailRequest(**EMAIL_DATA).dict()
NOT_REQUIRED_ATTR_CREATE_EMAIL_REQUEST_BODY = CreateEmailRequest(**EMAIL_DATA).dict(exclude={'subject'})
INVALID_ATTR_CREATE_EMAIL_REQUEST_BODY = {
    "smtp_address_from": "test_from@123mail.com",
    "smtp_address_to": "test_to@123mail.com",
    "subject": {'key': 'val'},
}
