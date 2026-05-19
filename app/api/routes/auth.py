from fastapi import APIRouter, Depends, Form
from sqlalchemy.orm import Session
from app.services.users_service import UsersService
from app.api.dependencies import get_db

router = APIRouter()


@router.post("/login")
def login(name: str = Form(...), password: str = Form(...)):
    usersService = UsersService()
    user = usersService.login(name, password)

    if not user:
        return {'error': 'Не правильный логин или пароль'}
    return {'message': 'Authorized'}


@router.post('/register')
def register(
    username: str = Form(...),
    email: str = Form(...),
    password: str = Form(...),
    db: Session = Depends(get_db)
):
    userService = UsersService(db)
    result = userService.register(username, email, password)
    return result
