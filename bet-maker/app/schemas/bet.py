from enum import Enum
from decimal import Decimal
from pydantic import BaseModel


class BetCreate(BaseModel):
    event_id: str
    amount: float


class BetStatusEnum(str, Enum):
    PENDING = "PENDING"
    WON = "WON"
    LOST = "LOST"


class BetResponse(BaseModel):
    bet_id: str
    event_id: str
    amount: Decimal
    status: BetStatusEnum
