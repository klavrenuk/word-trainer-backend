from app.services.mock_data import MOCK_USER

fakeUserName = 'kirill'
fakeUserPassword = '123'

class UserService:
    def get_user(self):
        return MOCK_USER
    
    def login(self, name:str, password:str):
        if name == fakeUserName and password == fakeUserPassword:
            return MOCK_USER
        
        return None