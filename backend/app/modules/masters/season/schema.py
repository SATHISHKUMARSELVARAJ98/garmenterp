from datetime import date
from pydantic import BaseModel
from app.common.enums import SeasonStatus

class SeasonCreate(BaseModel):
    season_code: str
    season_name: str
    start_date: date | None = None
    end_date: date | None = None

class SeasonUpdate(BaseModel):
    season_name: str | None = None
    start_date: date | None = None
    end_date: date | None = None

class SeasonResponse(BaseModel):
    id: int
    season_code: str
    season_name: str
    start_date: date | None
    end_date: date | None
    status: SeasonStatus

    class Config:
        from_attributes = True
