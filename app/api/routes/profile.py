from fastapi import APIRouter, Form
from app.services.users_service import UsersService

router = APIRouter()

@router.get('/api/profile')
def get_profile():
        usersService = UsersService()
        return usersService.get_user()

@router.put('/api/profile')
def update_profile(
        user_id: int = Form(...),
        name: str = Form(...),
        email: str = Form(...),
        db: Session = Depends(get_db)
):
        usersServices = usersService(db)
        return service.update_user(name, email)