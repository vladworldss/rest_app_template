import uuid

from datetime import datetime

from app.entities.email import EmailBody

STATIC_UUID = uuid.UUID('8322d7d8-d138-4a17-8019-b386b4a79466')
STATIC_DT = datetime.now()

EMAIL_DATA = {
    'id': STATIC_UUID,
    "smtp_address_from": "test_from@123mail.com",
    "smtp_address_to": "test_to@123mail.com",
    "subject": "test_title",
    "body": "some body text",
    "send_date": STATIC_DT,
    "status": 0,
}

EMAIL_BODY = EmailBody(**EMAIL_DATA)
