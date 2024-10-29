from typing import Optional
import aiohttp
from app.schemas.event import Event
from app.config import settings


class EventRepository:
    def __init__(self):
        self.base_url = settings.line_provider_url

    async def get_event(self, event_id: str) -> Optional[Event]:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                f"{self.base_url}/events/event/{event_id}"
            ) as response:
                if response.status == 200:
                    data = await response.json()
                    return Event(**data)
                return None
