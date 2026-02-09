from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.modules.masters.color.schema import ColorCreate, ColorResponse
from app.modules.masters.color.service import ColorService

router = APIRouter(
    prefix="/colors",
    tags=["Color Master"]
)


@router.post("/", response_model=ColorResponse)
def create_color(
    data: ColorCreate,
    db: Session = Depends(get_db)
):
    return ColorService.create_color(db, data)


@router.get("/", response_model=List[ColorResponse])
def get_colors(db: Session = Depends(get_db)):
    return ColorService.list_colors(db)
