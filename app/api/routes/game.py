from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from app.services.game_service import GameService

router = APIRouter(prefix="/api/game", tags=["game"])

@router.post('/finish')
def round_finish(
    answers: list = Body(...),
    db: Session = Depends(get_db)
):
    user_id = 1
    
    game_service = GameService(db)
    game_service.finish_round(user_id, answers)
    
    return {"message": "Раунд завершён", "status": "ok"}