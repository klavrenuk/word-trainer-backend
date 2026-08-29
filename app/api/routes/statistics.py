from fastapi import APIRouter, Depends, Body
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from app.services.statistics_service import StatisticsService

router = APIRouter(prefix="/api/statistics", tags=["statistics"])

@router.get('/')
def statistics(
    user_id: int,
        db: Session = Depends(get_db)
):
    service_statistics = StatisticsService(db)
    return service_statistics.get_user_statistics(user_id)