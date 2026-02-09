from pydantic import BaseModel
from datetime import datetime


class ColorCreate(BaseModel):
    color_code: str
    color_name: str


class ColorResponse(BaseModel):
    color_id: int
    color_code: str
    color_name: str
    is_active: bool
    created_at: datetime

    class Config:
        from_attributes = True
