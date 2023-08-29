import pytest

from app.db.repositories.email.exceptions import EmailRepoError
from tests.unit.testdata import EMAIL_BODY

pytestmark = pytest.mark.asyncio


async def test_create_email_ok(email_repo, email_repo_save_ok_mock):
    await email_repo.create_email(EMAIL_BODY)


async def test_create_email_error(email_repo, email_repo_save_error_mock):
    with pytest.raises(EmailRepoError):
        await email_repo.create_email(EMAIL_BODY)


async def test_get_email_ok(email_repo, email_repo_get_ok_mock):
    await email_repo.get_email(EMAIL_BODY.id)


async def test_get_email_error(email_repo, email_repo_get_error_mock):
    with pytest.raises(EmailRepoError):
        await email_repo.get_email(EMAIL_BODY.id)
