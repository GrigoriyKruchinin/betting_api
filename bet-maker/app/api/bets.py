from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.database import get_db
from app.repositories.bet_repository import BetRepository
from app.schemas.bet import BetCreate, BetResponse

router = APIRouter()
bet_repo = BetRepository()


@router.post("/bet", response_model=dict)
async def create_bet(bet_data: BetCreate, db: AsyncSession = Depends(get_db)):
    bet = await bet_repo.create_bet(
        db=db, event_id=bet_data.event_id, amount=bet_data.amount
    )
    return {"bet_id": bet.bet_id, "status": bet.status}


@router.get("/bets", response_model=list[BetResponse])
async def get_bets(db: AsyncSession = Depends(get_db)):
    return await bet_repo.get_all_bets(db=db)
