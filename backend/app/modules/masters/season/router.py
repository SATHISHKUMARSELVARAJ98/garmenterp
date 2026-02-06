from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.modules.masters.season.schema import (
    SeasonCreate, SeasonUpdate, SeasonResponse
)
from app.modules.masters.season.repository import SeasonRepository
from app.modules.masters.season.service import SeasonService

router = APIRouter(
    prefix="/masters/seasons",
    tags=["Season Master"]
)

@router.post("/", response_model=SeasonResponse)
def create_season(data: SeasonCreate, db: Session = Depends(get_db)):
    return SeasonService.create(db, data)

@router.get("/", response_model=list[SeasonResponse])
def list_seasons(db: Session = Depends(get_db)):
    return SeasonRepository.get_all(db)

@router.put("/{season_id}", response_model=SeasonResponse)
def update_season(
    season_id: int,
    data: SeasonUpdate,
    db: Session = Depends(get_db)
):
    season = SeasonRepository.get_by_id(db, season_id)
    if not season:
        raise HTTPException(status_code=404, detail="Season not found")

    return SeasonService.update(db, season, data)
