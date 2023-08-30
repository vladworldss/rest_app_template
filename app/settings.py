import os
import pathlib

from functools import cache

from pydantic import BaseModel, Field, validator

import config_loader

BASE_DIR = pathlib.Path(__file__).parent.parent


class ImmutableBaseModel(BaseModel):
    class Config:
        allow_mutation = False
        extra = 'forbid'
        underscore_attrs_are_private = True

    def __hash__(self) -> int:
        return hash(str(self))


class ServerSettings(ImmutableBaseModel):
    host: str
    port: int
    debug: bool


class DBSettings(ImmutableBaseModel):
    host: str
    port: int
    user: str
    password: str
    database: str
    min_size: int = Field(..., description='Минимальное количество соединений в пуле')
    max_size: int = Field(..., description='Максимальное количество соединений в пуле')
    max_queries: int = Field(
        ..., description='Количество запросов после выполнения которых, соединение закрывается и заменяется новым'
    )
    max_inactive_connection_lifetime: float = Field(
        ...,
        description=(
            '''Время (в секундах), после которых неактивные соединения
                в пуле будут закрыты. Установите значение 0, если
                необходимо отключить этот механизм
            '''
        ),
    )

    @validator('host', 'user', 'password', 'database', pre=True)
    def make_strict_string(cls, val: str) -> str:
        # tomlkit имеет свой строковый тип String, который не подходит для asyncpg - приводим к стандартному
        return str(val)

    @property
    def dsn(self) -> str:
        return f'postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}'

    @property
    def masked_dsn(self) -> str:
        return f'postgresql://******:******@{self.host}:{self.port}/{self.database}'


class Settings(ImmutableBaseModel):
    server: ServerSettings
    database: DBSettings


@cache
def get_settings() -> Settings:
    path_to_config = os.getenv('CONFIG_PATH', str(BASE_DIR / 'config.toml'))
    return Settings(**config_loader.load_config(path_to_config=path_to_config))
