from fastapi import APIRouter
from app.services.users_service import UserService

router = APIRouter()

@router.get('/api/profile')
def get_profile():
        service = UserService()
        return service.get_user()