from sqlalchemy.orm import Session
from app.modules.masters.season.model import Season

class SeasonRepository:

    @staticmethod
    def create(db: Session, season: Season):
        db.add(season)
        db.commit()
        db.refresh(season)
        return season

    @staticmethod
    def get_all(db: Session):
        return db.query(Season).filter(Season.is_deleted == False).all()

    @staticmethod
    def get_by_id(db: Session, season_id: int):
        return db.query(Season).filter(
            Season.id == season_id,
            Season.is_deleted == False
        ).first()
