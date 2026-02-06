from pydantic import BaseModel
from enum import Enum


class BuyerStatus(str, Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class BuyerCreate(BaseModel):
    buyer_code: str
    buyer_name: str


class BuyerUpdate(BaseModel):
    buyer_name: str | None = None
    status: BuyerStatus | None = None


class BuyerResponse(BaseModel):
    id: int
    buyer_code: str
    buyer_name: str
    status: BuyerStatus

    class Config:
        from_attributes = True
