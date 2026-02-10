from sqlalchemy.orm import Session
from app.modules.masters.size.model import Size
from app.modules.masters.size.schema import SizeCreate


class SizeRepository:

    @staticmethod
    def create(db: Session, data: SizeCreate) -> Size:
        size = Size(
            size_code=data.size_code,
            size_name=data.size_name,
            size_type=data.size_type
        )
        db.add(size)
        db.commit()
        db.refresh(size)
        return size

    @staticmethod
    def get_all(db: Session):
        return db.query(Size).filter(Size.is_active == True).all()
