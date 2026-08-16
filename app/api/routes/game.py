from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from app.services.game_service import GameService

router = APIRouter(prefix="/api/game", tags=["game"])

@router.post('/finish')
def round_finish(
    user_id: int = Body(...),
    answers: list = Body(...),
    db: Session = Depends(get_db)
):
    game_service = GameService(db)
    game_service.finish_round(user_id, answers)
    
    return {"message": "Раунд завершён", "status": "ok"}

@router.get('/start')
def game_start(
        user_id: int,
        db: Session = Depends(get_db)
):
    game_service = GameService(db)
    list_words = game_service.start_round(user_id)

    return list_words