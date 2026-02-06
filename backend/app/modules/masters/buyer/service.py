from sqlalchemy.orm import Session
from . import repository
from .schema import BuyerCreate, BuyerUpdate


def create_buyer(db: Session, data: BuyerCreate):
    return repository.create_buyer(db, data)


def list_buyers(db: Session):
    return repository.get_all_buyers(db)


def update_buyer(db: Session, buyer_id: int, data: BuyerUpdate):
    buyer = repository.get_buyer_by_id(db, buyer_id)
    if not buyer:
        return None
    return repository.update_buyer(db, buyer, data)
