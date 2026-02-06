from sqlalchemy import Column, Integer, String, Date, Boolean, Enum
from app.core.database import Base
from app.common.enums import SeasonStatus

class Season(Base):
    __tablename__ = "season_master"

    id = Column(Integer, primary_key=True, index=True)
    season_code = Column(String(20), nullable=False)
    season_name = Column(String(100), nullable=False)
    start_date = Column(Date)
    end_date = Column(Date)
    status = Column(Enum(SeasonStatus), default=SeasonStatus.ACTIVE)
    is_deleted = Column(Boolean, default=False)
