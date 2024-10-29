from pydantic import BaseModel
from typing import Optional
from enum import Enum
import decimal


class EventState(str, Enum):
    NEW = "NEW"
    FINISHED_WIN = "FINISHED_WIN"
    FINISHED_LOSE = "FINISHED_LOSE"


class Event(BaseModel):
    event_id: str
    coefficient: Optional[decimal.Decimal]
    deadline: Optional[int]
    state: Optional[EventState]


class EventUpdate(BaseModel):
    state: EventState
