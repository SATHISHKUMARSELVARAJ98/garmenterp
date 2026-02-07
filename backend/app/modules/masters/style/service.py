from sqlalchemy.orm import Session
from . import repository
from .schema import StyleCreate, StyleUpdate


def create_style(db: Session, data: StyleCreate):
    return repository.create_style(db, data)


def list_styles(db: Session):
    return repository.get_all_styles(db)


def update_style(db: Session, style_id: int, data: StyleUpdate):
    style = repository.get_style_by_id(db, style_id)
    if not style:
        return None
    return repository.update_style(db, style, data)
