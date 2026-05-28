from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from app.services.users_service import UsersService
from app.api.dependencies import get_db

router = APIRouter()


@router.post("/login")
def login(login: str = Form(...), password: str = Form(...)):
    usersService = UsersService()
    user = usersService.login(login, password)

    if not user:
        return {'error': 'Не правильный логин или пароль'}
    return {'message': 'Authorized'}


@router.post('/register')
def register(
    login: str = Form(...),
    name: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    userService = UsersService(db)
    result = userService.register(login, name, password)
    return result


@router.get('/api/auth/me')
def get_current_user(
    db: Session = Depends(get_db)
):
    user_service = UsersService(db)
    user = user_service.get_first_user()
    
    if not user:
        return {'error': 'User not found'}
    
    return {
        'id': user.id,
        'username': user.username,
        'email': user.email
    }