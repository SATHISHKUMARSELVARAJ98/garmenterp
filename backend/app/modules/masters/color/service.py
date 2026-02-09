from sqlalchemy.orm import Session
from app.modules.masters.color.repository import ColorRepository
from app.modules.masters.color.schema import ColorCreate


class ColorService:

    @staticmethod
    def create_color(db: Session, data: ColorCreate):
        return ColorRepository.create(db, data)

    @staticmethod
    def list_colors(db: Session):
        return ColorRepository.get_all(db)
