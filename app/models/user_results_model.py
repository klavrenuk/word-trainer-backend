from sqlalchemy import Column, Integer, ForeignKey, Boolean
from app.core.database import Base

class UserResult(Base):
    __tablename__ = "user_results"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    word_id = Column(Integer, ForeignKey("words.id"), nullable=False)
    is_learned = Column(Boolean, default=False)