from pydantic import BaseModel, Field
from enum import Enum


class StyleStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class StyleCreate(BaseModel):
    style_code: int = Field(..., ge=100000, le=999999)
    style_name: str


class StyleUpdate(BaseModel):
    style_name: str | None = None
    status: StyleStatus | None = None


class StyleResponse(BaseModel):
    style_master_id: int
    style_code: int
    style_name: str
    status: StyleStatus

    class Config:
        from_attributes = True
