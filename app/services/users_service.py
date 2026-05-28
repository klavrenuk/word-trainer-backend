from app.services.mock_data import MOCK_USER
from app.models.user import User
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

class UsersService:
    def __init__(self, db: Session = None):
        self.db = db
    
    def get_user(self):
        return MOCK_USER
    
    def login(self, login:str, password:str): 
       user = self.db.query(User).filter(User.username == name).first()
       if not user:
           return None
       
       if pwd_context.verify(password, user.password):
           return user
            
    def register(self, login:str, name:str, password:str):
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
            'username': new_user.username,
            'email': new_user.email
        }
        
    def update_user(self, user_id: int, name: str):
        user = self.db.query(User).filter(User.id == user_id).first()
        
        if not user:
            return {'error': 'User not found'}
        
        user.username = name
        
        self.db.commit()
        self.db.refresh(user)
        
        return {
            'user': user,
            'message': 'Profile updated successfully'
        }
        
    def get_first_user(self):
        return self.db.query(User).first()