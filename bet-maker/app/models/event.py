from enum import Enum as PyEnum
from sqlalchemy import DECIMAL, Integer, String, Enum
from sqlalchemy.orm import Mapped, mapped_column
from app.db.base import Base


class EventState(PyEnum):
    NEW = "NEW"
    FINISHED_WIN = "FINISHED_WIN"
    FINISHED_LOSE = "FINISHED_LOSE"


class Event(Base):
    __tablename__ = "events"

    event_id: Mapped[str] = mapped_column(String, primary_key=True, index=True)
    coefficient: Mapped[float] = mapped_column(DECIMAL(5, 2), nullable=False)
    deadline: Mapped[int] = mapped_column(Integer, nullable=False)
    state: Mapped[EventState] = mapped_column(Enum(EventState), default=EventState.NEW)
