from datetime import datetime, timezone
from sqlalchemy import Boolean, Column, DateTime, Integer, String, UUID
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, mapped_column, Mapped

from .database import Base


class Lift(Base):
    __tablename__ = "lifts"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    lift_key: Mapped[UUID] = mapped_column(unique=True, index=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"), index=True)
    name: Mapped[str] = mapped_column(String, index=True)
    training_max: Mapped[int] = mapped_column(Integer)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False)
    created_date: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc)
    )
    modified_date: Mapped[datetime] = mapped_column(
        DateTime, default=datetime.now(timezone.utc)
    )

    # id = Column(Integer, primary_key=True, index=True)
    # lift_key = Column(UUID, unique=True, index=True)
    # user_id = Column(Integer, foreign_key index=True)
    # name = Column(String, unique=True, index=True)
    # training_max = Column(Integer)
    # is_active = Column(Boolean, default=True)
    # is_deleted = Column(Boolean, default=False)
    # created_date = Column(DateTime, default=datetime.now(timezone.utc))
    # modified_date = Column(DateTime, default=datetime.now(timezone.utc))
    # created_by_user = Column(UUID)
