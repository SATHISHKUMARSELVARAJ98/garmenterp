from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from .schema import StyleCreate, StyleUpdate, StyleResponse
from .service import create_style, list_styles, update_style

router = APIRouter(
    prefix="/masters/styles",
    tags=["Style Master"]
)


@router.post("/", response_model=StyleResponse)
def create(data: StyleCreate, db: Session = Depends(get_db)):
    return create_style(db, data)


@router.get("/", response_model=list[StyleResponse])
def list_all(db: Session = Depends(get_db)):
    return list_styles(db)


@router.put("/{style_id}", response_model=StyleResponse)
def update(style_id: int, data: StyleUpdate, db: Session = Depends(get_db)):
    style = update_style(db, style_id, data)
    if not style:
        raise HTTPException(status_code=404, detail="Style not found")
    return style
