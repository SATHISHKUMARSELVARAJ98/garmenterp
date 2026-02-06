from sqlalchemy.orm import Session
from app.modules.masters.season.domain.entity import SeasonEntity
from app.modules.masters.season.domain.aggregate import SeasonAggregate
from app.modules.masters.season.model import Season
from app.modules.masters.season.schema import SeasonCreate, SeasonUpdate

class SeasonService:

    @staticmethod
    def create(db: Session, data: SeasonCreate):
        season = Season(**data.dict())
        db.add(season)
        db.commit()
        db.refresh(season)
        return season

    @staticmethod
    def update(db: Session, season: Season, data: SeasonUpdate):
        entity = SeasonEntity(
            season_code=season.season_code,
            season_name=season.season_name,
            start_date=season.start_date,
            end_date=season.end_date,
            status=season.status
        )

        aggregate = SeasonAggregate(entity)
        aggregate.update_details(
            season_name=data.season_name,
            start_date=data.start_date,
            end_date=data.end_date
        )

        season.season_name = entity.season_name
        season.start_date = entity.start_date
        season.end_date = entity.end_date

        db.commit()
        return season
