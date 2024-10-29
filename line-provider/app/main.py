from fastapi import FastAPI
from app.api import events

app = FastAPI(title="Line Provider Service")
app.include_router(events.router, prefix="/events", tags=["line-provider events"])


