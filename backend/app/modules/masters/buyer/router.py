from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.database import get_db
from .schema import BuyerCreate, BuyerUpdate, BuyerResponse
from .service import create_buyer, list_buyers, update_buyer

router = APIRouter(
    prefix="/masters/buyers",
    tags=["Buyer Master"]
)


@router.post("/", response_model=BuyerResponse)
def create(data: BuyerCreate, db: Session = Depends(get_db)):
    return create_buyer(db, data)


@router.get("/", response_model=list[BuyerResponse])
def list_all(db: Session = Depends(get_db)):
    return list_buyers(db)


@router.put("/{buyer_id}", response_model=BuyerResponse)
def update(buyer_id: int, data: BuyerUpdate, db: Session = Depends(get_db)):
    buyer = update_buyer(db, buyer_id, data)
    if not buyer:
        raise HTTPException(status_code=404, detail="Buyer not found")
    return buyer
