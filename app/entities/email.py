from datetime import datetime
from typing import Optional

from pydantic import Field

from app.entities.enums import EmailStatus

from .base import BaseEntity


class EmailBody(BaseEntity):
    smtp_address_from: str
    smtp_address_to: str
    subject: str
    body: Optional[str]
    send_date: datetime = Field(default_factory=datetime.now)
    status: EmailStatus = EmailStatus.DRAFT
