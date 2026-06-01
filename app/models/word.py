from sqlalchemy import Column, Integer, String
from app.core.database import Base


class Word(Base):
    __tablename__ = "words"

    id = Column(Integer, primary_key=True, index=True)  # первичный ключ
    word = Column(String, nullable=False, index=True)  # английское слово
    translation = Column(String, nullable=False)  # русский перевод
    # транскрипция (необязательное поле)
    transcription = Column(String, nullable=True)
