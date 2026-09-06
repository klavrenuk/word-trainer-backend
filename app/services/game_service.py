from sqlalchemy.orm import Session
from app.models.user_mistake import UserMistake
from app.repositories.game_repository import GameRepository

class GameService:
    def __init__(self, db:Session):
        self.db = db
        self.game_repository = GameRepository(db)
        
    def finish_round(self, user_id: int, answers: list):
        for answer in answers:
            if not answer['is_correct']:
                new_mistake = UserMistake(
                    user_id=user_id,
                    word_id=answer['word_id']
                )
                
                self.db.add(new_mistake) 
                
        self.db.commit()

    def start_round(self, user_id: int, count_words:int):
        mistake_words = self.game_repository.get_mistake_words(user_id, count_words)

        if len(mistake_words) < count_words:
            mistake_ids = [word.id for word in mistake_words]

            new_words = self.game_repository.get_new_words(mistake_ids, count_words - len(mistake_words))
            mistake_words.extend(new_words)

        return mistake_words