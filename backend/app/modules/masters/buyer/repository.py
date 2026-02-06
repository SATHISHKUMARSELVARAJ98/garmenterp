from sqlalchemy.orm import Session
from .model import Buyer
from .schema import BuyerCreate, BuyerUpdate


def create_buyer(db: Session, data: BuyerCreate) -> Buyer:
    buyer = Buyer(**data.model_dump())
    db.add(buyer)
    db.commit()
    db.refresh(buyer)
    return buyer


def get_all_buyers(db: Session):
    return db.query(Buyer).all()


def get_buyer_by_id(db: Session, buyer_id: int):
    return db.query(Buyer).filter(Buyer.id == buyer_id).first()


def update_buyer(db: Session, buyer: Buyer, data: BuyerUpdate):
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(buyer, field, value)
    db.commit()
    db.refresh(buyer)
    return buyer
