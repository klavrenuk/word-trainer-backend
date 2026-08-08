from sqlalchemy.orm import Session

from app.models.user_results import UserResult

class UserResultRepository:
    def __init__(self, db: Session):
        self.db = db

