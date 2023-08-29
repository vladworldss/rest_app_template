from functools import cache

import asyncpg

from app.db.repositories.email.repo import EmailRepository
from app.services.interfaces import IEmailRepository

from .settings import get_settings


@cache
def get_db_pool() -> asyncpg.Pool:
    return asyncpg.create_pool(get_settings().database.dsn, **get_settings().database.dict())


@cache
def get_email_repo() -> IEmailRepository:
    return EmailRepository(db_pool=get_db_pool())
