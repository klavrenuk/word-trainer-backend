from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.dependencies import get_db

from app.services.users_service import UsersService

router = APIRouter(prefix='/api/user')

@router.get('/{id}')
def getUser(
    id: int,
    db: Session = Depends(get_db)
):
    users_service = UsersService(db)
    return users_service.get_user(id)