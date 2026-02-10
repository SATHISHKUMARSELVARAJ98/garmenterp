from sqlalchemy.orm import Session
from app.modules.masters.size.repository import SizeRepository
from app.modules.masters.size.schema import SizeCreate


class SizeService:

    @staticmethod
    def create_size(db: Session, data: SizeCreate):
        return SizeRepository.create(db, data)

    @staticmethod
    def list_sizes(db: Session):
        return SizeRepository.get_all(db)
