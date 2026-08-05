from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.api.dependencies import get_db

from app.services.users_service import UsersService

router = APIRouter(prefix='/api/admin')

@router.get('/users')
def getUsers(db:Session = Depends(get_db)):
    users_service = UsersService(db)
    users = users_service.getUsers()
    return users
