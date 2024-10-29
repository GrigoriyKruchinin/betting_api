from fastapi import FastAPI
from app.api import events
from app.api import bets

app = FastAPI(title="Bet Maker Service")
app.include_router(events.router, prefix="/bm_events", tags=["bet-maker events"])
app.include_router(bets.router, prefix="/bets", tags=["bets"])
