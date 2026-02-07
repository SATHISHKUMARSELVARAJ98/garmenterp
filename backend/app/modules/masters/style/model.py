from sqlalchemy import Column, BigInteger, String, Enum
from app.core.database import Base
import enum


class StyleStatus(str, enum.Enum):
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"


class Style(Base):
    __tablename__ = "style_master"

    style_master_id = Column(
        BigInteger,
        primary_key=True,
        index=True
    )

    style_code = Column(
        BigInteger,
        unique=True,
        nullable=False,
        index=True
    )  # 6-digit numeric code

    style_name = Column(
        String(100),
        nullable=False
    )

    status = Column(
        Enum(StyleStatus),
        nullable=False,
        default=StyleStatus.ACTIVE
    )
