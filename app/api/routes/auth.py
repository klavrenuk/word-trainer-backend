from fastapi import APIRouter, Form
from app.services.users_service import UserService

router = APIRouter()

@router.post("/login")
def login(name: str = Form(...), password: str = Form(...)):
    userService = UserService()
    user = userService.login(name, password)
    
    if not user:
        return {'error': 'Не правильный логин или пароль'}
    return {'message': 'Authorized'}