from sqlalchemy import DECIMAL, String, Enum
from sqlalchemy.orm import Mapped, mapped_column
from enum import Enum as PyEnum
from app.db.base import Base


class BetStatus(PyEnum):
    PENDING = "PENDING"
    WON = "WON"
    LOST = "LOST"


class Bet(Base):
    __tablename__ = "bets"

    bet_id: Mapped[str] = mapped_column(String, primary_key=True, index=True)
    event_id: Mapped[str] = mapped_column(String, nullable=False)
    amount: Mapped[float] = mapped_column(DECIMAL(10, 2), nullable=False)
    status: Mapped[BetStatus] = mapped_column(
        Enum(BetStatus), default=BetStatus.PENDING
    )
