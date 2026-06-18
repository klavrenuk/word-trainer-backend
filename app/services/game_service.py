from sqlalchemy.orm import Session
from app.models.word import Word
from app.models.user_mistake import UserMistake

class GameService:
    def __init__(self, db:Session):
        self.db = db
        
    def finish_round(self, user_id: int, answers: list):
        for answer in answers:
            if not answer['is_correct']:
                new_mistake = UserMistake(
                    user_id=user_id,
                    word_id=answer['word_id']
                )
                
                self.db.add(new_mistake) 
                
        self.db.commit()