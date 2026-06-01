from sqlalchemy.orm import Session
from app.repositories.word_repository import WordsRepository


class WordsService:
    def __init__(self, db: Session):
        self.words_repository = WordsRepository(db)

    def get_all_words(self, offset: int = 0, page_size: int = 50):
        return self.words_repository.get_all(offset, page_size)
