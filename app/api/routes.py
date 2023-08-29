from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException
from starlette.responses import PlainTextResponse

from app.api.urls import CREATE_EMAIL, GET_EMAIL, HEALTH_PATH
from app.dependencies import get_email_repo
from app.entities.email import EmailBody
from app.services.interfaces import IEmailRepository

from .models import CreateEmailRequest, GetEmailRequest

app_router = APIRouter()


@app_router.get(HEALTH_PATH, response_class=PlainTextResponse)
async def health() -> str:
    return 'Healthy'


@app_router.get(GET_EMAIL)
async def get_email_by_id(
    request: GetEmailRequest, email_repo: IEmailRepository = Depends(get_email_repo)
) -> EmailBody:
    try:
        email = await email_repo.get_email(request.id)
        if not email:
            raise HTTPException(detail={'message': 'email not found'}, status_code=404)

        return email
    except Exception:
        raise HTTPException(detail={'message': 'Ошибка на сервере'}, status_code=500)


@app_router.post(CREATE_EMAIL)
async def create_email(request: CreateEmailRequest, email_repo: IEmailRepository = Depends(get_email_repo)) -> UUID:
    try:
        return await email_repo.create_email(EmailBody(**request.dict()))

    except Exception as e:
        raise HTTPException(detail={'message': f'Ошибка на сервере. {e}'}, status_code=500)
