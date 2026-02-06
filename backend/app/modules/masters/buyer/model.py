from sqlalchemy import Column, Integer, String, Enum
from app.core.database import Base
import enum


class BuyerStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class Buyer(Base):
    __tablename__ = "buyer_master"

    id = Column(Integer, primary_key=True, index=True)
    buyer_code = Column(String(50), unique=True, nullable=False)
    buyer_name = Column(String(100), nullable=False)
    status = Column(Enum(BuyerStatus), default=BuyerStatus.ACTIVE, nullable=False)
