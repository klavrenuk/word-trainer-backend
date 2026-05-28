from fastapi import APIRouter, Form, Depends
from app.services.users_service import UsersService
from sqlalchemy.orm import Session
from app.api.dependencies import get_db

router = APIRouter()

@router.get('/api/profile')
def get_profile():
        usersService = UsersService()
        return usersService.get_user()

@router.put('/api/profile')
def update_profile(
        user_id: int = Form(...),
        name: str = Form(...),
        db: Session = Depends(get_db)
):
        usersServices = UsersService(db)
        return usersServices.update_user(user_id, name)