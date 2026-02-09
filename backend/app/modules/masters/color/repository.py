from sqlalchemy.orm import Session
from app.modules.masters.color.model import Color
from app.modules.masters.color.schema import ColorCreate


class ColorRepository:

    @staticmethod
    def create(db: Session, data: ColorCreate) -> Color:
        color = Color(
            color_code=data.color_code,
            color_name=data.color_name
        )
        db.add(color)
        db.commit()
        db.refresh(color)
        return color

    @staticmethod
    def get_all(db: Session):
        return db.query(Color).filter(Color.is_active == True).all()
