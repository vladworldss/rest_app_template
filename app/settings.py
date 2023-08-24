import pathlib

from functools import cache
from typing import Any
import config_loader

from pydantic import BaseModel, Field, PrivateAttr

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


class Settings(ImmutableBaseModel):
    server: ServerSettings


@cache
def get_settings() -> Settings:
    return Settings(**config_loader.load_config(path_to_config=str(BASE_DIR / 'config.toml')))
