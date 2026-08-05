from fastapi import APIRouter, Form, Depends, Body
from app.services.users_service import UsersService
from sqlalchemy.orm import Session
from app.api.dependencies import get_db

router = APIRouter()

@router.get('/api/profile')
def get_profile():
        users_service = UsersService()
        return users_service.get_user()

@router.put('/api/profile')
def update_profile(
        user_id: int = Form(...),
        name: str = Form(...),
        db: Session = Depends(get_db)
):
        users_service = UsersService(db)
        return users_service.update_user(user_id, name)

@router.put('/api/password')
def update_password(
        oldPassword: str = Body(...),
        newPassword: str = Body(...),
        userId: int = Body(...),
        db: Session = Depends(get_db)
):
        users_services = UsersService(db)
        return users_services.update_password(userId, oldPassword, newPassword)
