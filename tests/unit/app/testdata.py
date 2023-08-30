from app.api.models import CreateEmailRequest
from tests.unit.testdata import EMAIL_DATA

CREATE_EMAIL_REQUEST_BODY = CreateEmailRequest(**EMAIL_DATA).dict()
