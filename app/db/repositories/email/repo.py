from typing import Optional
from uuid import UUID

import asyncpg

from app.entities.email import EmailBody
from app.services.interfaces import IEmailRepository


class EmailRepository(IEmailRepository):
    def __init__(self, db_pool: asyncpg.Pool):
        self._db_pool = db_pool

    @property
    def _get_email_sql(self) -> str:
        return """
        SELECT * from emails.email
        WHERE id=$1;
        """

    @property
    def _create_email(self) -> str:
        return """
        INSERT INTO emails.email
        (SELECT * from UNNEST($1::emails.email[]))
        RETURNING id;
        """

    async def get_email(self, id: UUID) -> Optional[EmailBody]:
        async with self._db_pool.acquire() as conn:
            res = await conn.fetchrow(self._get_email_sql, id)
        if res:
            return EmailBody(**res)

    async def create_email(self, email: EmailBody) -> UUID:
        async with self._db_pool.acquire() as conn:
            email_id = await conn.fetchval(self._create_email, [tuple(email.dict().values())])

        return email_id
