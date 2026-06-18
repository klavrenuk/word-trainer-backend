from sqlalchemy.orm import Session
from app.models.word import Word
from app.models.user_mistake import UserMistake

class StatisticsService:
    def __init__(self, db: Session):
        self.db = db
        
    def get_mistakes_count(self, user_id: int):
        return self.db.query(UserMistake).filter(UserMistake.user_id == user_id).count()