import uuid

from typing import TypeVar

from pydantic import BaseModel, Extra, Field


class BaseEntity(BaseModel):
    id: uuid.UUID = Field(default_factory=uuid.uuid4)

    class Config:
        extra = Extra.forbid
        validate_assignment = True


BaseEntityType = TypeVar('BaseEntityType', bound=BaseEntity)
