from sqlalchemy.orm import Session
from .model import Style
from .schema import StyleCreate, StyleUpdate


def create_style(db: Session, data: StyleCreate) -> Style:
    style = Style(**data.model_dump())
    db.add(style)
    db.commit()
    db.refresh(style)
    return style


def get_all_styles(db: Session):
    return db.query(Style).all()


def get_style_by_id(db: Session, style_id: int):
    return (
        db.query(Style)
        .filter(Style.style_master_id == style_id)
        .first()
    )


def update_style(db: Session, style: Style, data: StyleUpdate):
    for field, value in data.model_dump(exclude_unset=True).items():
        setattr(style, field, value)
    db.commit()
    db.refresh(style)
    return style
