from app.services.mock_data import MOCK_USER
from app.models.user import User

fakeUserName = 'kirill'
fakeUserPassword = '123'

class UsersService:
    
    def __init__(self, db: Session = None):
        self.db = db
    
    def get_user(self):
        return MOCK_USER
    
    def login(self, name:str, password:str):
        if name == fakeUserName and password == fakeUserPassword:
            return MOCK_USER
        
        return None
    
    def register(self, username:str, email:str, password:str):
        existing_user = self.db.query(User).filter(User.username == username).first()
        if existing_user:
            return {'error': 'Username already exist'}
        
        new_user = User(
            username=username,
            email=email,
            password=password
        )
        
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        
        return {
            'id': new_user.id,
            'username': new_user.username,
            'email': new_user.email
        }
        
    def update_user(self, user_id: int, name: str, email: str):
        user = self.db.query(User).filter(User.id == user_id).first()
        
        if not user:
            return {'error': 'User not found'}
        
        user.username = name
        user.email = email
        
        self.db.commit()
        self.db.refresh(user)
        
        return {
            'user': user,
            'message': 'Profile updated successfully'
        }