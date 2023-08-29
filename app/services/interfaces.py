import abc

from typing import Optional
from uuid import UUID

from app.entities.email import EmailBody
from app.entities.request_log import RequestLog


class IRequestLogRepository(abc.ABC):
    @abc.abstractmethod
    async def save(self, request_log: RequestLog) -> None:
        pass


class IEmailRepository(abc.ABC):
    @abc.abstractmethod
    async def get_email(self, id: UUID) -> Optional[EmailBody]:
        pass

    @abc.abstractmethod
    async def create_email(self, email: EmailBody) -> UUID:
        pass
