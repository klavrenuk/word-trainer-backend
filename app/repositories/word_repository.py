from sqlalchemy.orm import Session
from app.models.word import Word

class WordsRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_all(self, offset: int = 0, page_size: int = 50):
        return self.db.query(Word).offset(offset).limit(page_size).all()