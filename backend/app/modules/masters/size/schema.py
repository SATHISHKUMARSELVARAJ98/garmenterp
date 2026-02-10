from pydantic import BaseModel
from datetime import datetime


class SizeCreate(BaseModel):
    size_code: str
    size_name: str
    size_type: str


class SizeResponse(BaseModel):
    size_id: int
    size_code: str
    size_name: str
    size_type: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True
