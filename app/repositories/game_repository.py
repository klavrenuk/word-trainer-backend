from sqlalchemy.orm import Session
from app.models.user_mistake import UserMistake
from app.models.word import Word
from app.core.constants import ROUND_WORDS_LIMIT

class GameRepository():
    def __init__(self, db: Session):
        self.db = db

    def get_mistake_words(self, user_id: int, limit: int = ROUND_WORDS_LIMIT):
        return self.db.query(Word).join(
            UserMistake, UserMistake.word_id == Word.id
        ).filter(UserMistake.user_id == user_id).limit(limit).all()

    def get_new_words(self, exclude_ids: list = [], limit: int = ROUND_WORDS_LIMIT):
        if not exclude_ids:
            return self.db.query(Word).limit(limit).all()
        return self.db.query(Word).filter(
            Word.id.not_in(exclude_ids)
        ).limit(limit).all()