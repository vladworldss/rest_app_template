from typing import Optional

from pydantic import BaseModel


class CreateEmailRequest(BaseModel):
    smtp_address_from: str
    smtp_address_to: str
    subject: str
    body: Optional[str]
