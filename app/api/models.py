from typing import Optional
from uuid import UUID

from pydantic import BaseModel


class GetEmailRequest(BaseModel):
    id: UUID


class CreateEmailRequest(BaseModel):
    smtp_address_from: str
    smtp_address_to: str
    subject: str
    body: Optional[str]
