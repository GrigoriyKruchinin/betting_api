from fastapi import APIRouter, HTTPException, Depends
from app.schemas.event import Event, EventUpdate
from app.repositories.event_repository import EventRepository, get_event_repository

router = APIRouter()


@router.post("/event", response_model=dict)
async def create_event(
    event: Event, event_repo: EventRepository = Depends(get_event_repository)
):
    await event_repo.add_event(event)
    return {"message": "Event created"}


@router.patch("/event/{event_id}", response_model=dict)
async def update_event(
    event_id: str,
    event_data: EventUpdate,
    event_repo: EventRepository = Depends(get_event_repository),
):
    updated_event = await event_repo.update_event(
        event_id, event_data.dict(exclude_unset=True)
    )
    if not updated_event:
        raise HTTPException(status_code=404, detail="Event not found")
    return {"message": "Event status updated"}


@router.get("/event/{event_id}", response_model=Event)
async def get_event(
    event_id: str, event_repo: EventRepository = Depends(get_event_repository)
):
    event = await event_repo.get_event(event_id)
    if not event:
        raise HTTPException(status_code=404, detail="Event not found")
    return event


@router.get("/events", response_model=list[Event])
async def get_active_events(
    event_repo: EventRepository = Depends(get_event_repository),
):
    return await event_repo.get_active_events()
