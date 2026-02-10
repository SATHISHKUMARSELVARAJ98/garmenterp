from sqlalchemy import BigInteger, String, Boolean, DateTime, func
from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class Size(Base):
    __tablename__ = "size_master"

    size_id: Mapped[int] = mapped_column(
        BigInteger,
        primary_key=True
    )

    size_code: Mapped[str] = mapped_column(
        String(20),
        unique=True,
        nullable=False
    )

    size_name: Mapped[str] = mapped_column(
        String(50),
        nullable=False
    )

    size_type: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )  # ALPHA / NUMERIC / MIXED

    is_active: Mapped[bool] = mapped_column(
        Boolean,
        default=True,
        nullable=False
    )

    created_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    updated_at: Mapped[DateTime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now()
    )
