from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List

from app.core.database import get_db
from app.modules.masters.size.schema import SizeCreate, SizeResponse
from app.modules.masters.size.service import SizeService

router = APIRouter(
    prefix="/sizes",
    tags=["Size Master"]
)


@router.post("/", response_model=SizeResponse)
def create_size(
    data: SizeCreate,
    db: Session = Depends(get_db)
):
    return SizeService.create_size(db, data)


@router.get("/", response_model=List[SizeResponse])
def get_sizes(db: Session = Depends(get_db)):
    return SizeService.list_sizes(db)
