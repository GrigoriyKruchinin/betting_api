from typing import Dict, Optional, List
from app.schemas.event import Event, EventState


class EventRepository:
    def __init__(self):
        self.events: Dict[str, Event] = {}

    async def add_event(self, event: Event) -> None:
        self.events[event.event_id] = event

    async def update_event(self, event_id: str, data: dict) -> Optional[Event]:
        event = self.events.get(event_id)
        if event:
            for key, value in data.items():
                setattr(event, key, value)
            return event
        return None

    async def get_event(self, event_id: str) -> Optional[Event]:
        return self.events.get(event_id)

    async def get_active_events(self) -> List[Event]:
        return [
            event for event in self.events.values() if event.state == EventState.NEW
        ]


event_repository = EventRepository()


async def get_event_repository() -> EventRepository:
    return event_repository
