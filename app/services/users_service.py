import jwt

from app.services.mock_data import MOCK_USER
from app.models.user import User
from passlib.context import CryptContext
from sqlalchemy.orm import Session
from datetime import datetime, timedelta

from app.core.config import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class UsersService:
    def __init__(self, db: Session = None):
        self.db = db

    def get_user(self):
        return MOCK_USER
    
    def create_access_token(self, data: dict):
        to_encode = data.copy()
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
        to_encode.update({'exp': expire})
        
        return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        

    def login(self, login: str, password: str):
        user = self.db.query(User).filter(User.login == login).first()
        if not user:
            return None

        if not pwd_context.verify(password, user.password):
            return None
        
        access_token = self.create_access_token(data={
            'sub': user.login,
            'user_id': user.id
        })
        
        return {
            'access_token': access_token,
            'token_type': 'bearer',
            'user_id': user.id,
            'login': user.login,
            'name': user.name
        }


    def register(self, login: str, name: str, password: str):
        existing_user = self.db.query(User).filter(User.login == login).first()
        if existing_user:
            return {'error': 'Username already exist'}

        hashed_password = pwd_context.hash(password)

        new_user = User(
            login=login,
            name=name,
            password=hashed_password
        )

        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)

        return {
            'id': new_user.id,
            'name': new_user.name,
            'login': new_user.login
        }

    def update_user(self, user_id: int, name: str):
        user = self.db.query(User).filter(User.id == user_id).first()

        if not user:
            return {'error': 'User not found'}

        user.name = name

        self.db.commit()
        self.db.refresh(user)

        return {
            'user': user,
            'message': 'Profile updated successfully'
        }

    def get_first_user(self):
        return self.db.query(User).first()