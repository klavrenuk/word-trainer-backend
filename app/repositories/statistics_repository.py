from sqlalchemy.orm import Session

from app.models.user_results import UserResult
from app.models.user_mistake import UserMistake

class StatisticsRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_user_learned_words(self, user_id:int):
        return self.db.query(UserResult).filter(
            UserResult.user_id == user_id
        ).all()

    def get_user_mistakes(self, user_id:int):
        return self.db.query(UserMistake).filter(UserMistake.user_id == user_id).all()