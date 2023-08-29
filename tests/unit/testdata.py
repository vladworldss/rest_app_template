from app.entities.email import EmailBody

EMAIL_DATA = {
    "id": "8322d7d8-d138-4a17-8019-b386b4a79466",
    "smtp_address_from": "test_from@123mail.com",
    "smtp_address_to": "test_to@123mail.com",
    "subject": "test_title",
    "body": "some body text",
    "send_date": "2023-08-29T12:23:35.116374",
    "status": 0,
}

EMAIL_BODY = EmailBody(**EMAIL_DATA)
