import pytest

from tests.unit.testdata import EMAIL_BODY


@pytest.fixture
def email_repo_save_ok_mock(when2, db_connection, async_result, email_repo):
    when2(db_connection.fetchval, email_repo._create_email_sql, [tuple(EMAIL_BODY.dict().values())]).thenReturn(
        async_result(EMAIL_BODY.id)
    )


@pytest.fixture
def email_repo_save_error_mock(when2, db_connection, async_result, email_repo):
    when2(db_connection.fetchval, email_repo._create_email_sql, [tuple(EMAIL_BODY.dict().values())]).thenRaise(
        Exception('Some DB exception')
    )


@pytest.fixture
def email_repo_get_ok_mock(when2, db_connection, async_result, email_repo):
    when2(db_connection.fetchrow, email_repo._get_email_sql, EMAIL_BODY.id).thenReturn(
        async_result(EMAIL_BODY.dict())
    )


@pytest.fixture
def email_repo_get_error_mock(when2, db_connection, async_result, email_repo):
    when2(db_connection.fetchrow, email_repo._get_email_sql, EMAIL_BODY.id).thenRaise(Exception('Some DB GET exception'))
