from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.dependencies import get_db

from app.services.statistics_service import StatisticsService

router = APIRouter(prefix='/api/results', tags=['results'])

@router.get('/')
def get_user_results(
    db: Session = Depends(get_db)
):
    user_id = 1
    
    statistics_service = StatisticsService(db)
    mistakes_count = statistics_service.get_mistakes_count(user_id)
    
    return {
        'mistakes_count': mistakes_count
    }
