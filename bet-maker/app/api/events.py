from fastapi import APIRouter, Depends, HTTPException
from app.repositories.event_repository import EventRepository

router = APIRouter()
event_repo = EventRepository()


@router.get("/event/{event_id}")
async def get_event(event_id: str):
    event = await event_repo.get_event(event_id)
    if event is None:
        raise HTTPException(status_code=404, detail="Event not found")
    return event
