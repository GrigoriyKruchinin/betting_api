from typing import List
from uuid import uuid4
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from app.models.bet import Bet, BetStatus


class BetRepository:
    async def create_bet(self, db: AsyncSession, event_id: str, amount: float) -> Bet:
        bet = Bet(
            bet_id=str(uuid4()),
            event_id=event_id,
            amount=amount,
            status=BetStatus.PENDING,
        )
        db.add(bet)
        await db.commit()
        await db.refresh(bet)
        return bet

    async def get_all_bets(self, db: AsyncSession) -> List[Bet]:
        result = await db.execute(select(Bet))
        return result.scalars().all()
