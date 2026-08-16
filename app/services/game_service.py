from sqlalchemy.orm import Session
from app.models.user_mistake import UserMistake
from app.repositories.game_repository import GameRepository

from app.core.constants import ROUND_WORDS_LIMIT

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

    def start_round(self, user_id):
        mistake_words = self.game_repository.get_mistake_words(user_id, ROUND_WORDS_LIMIT)

        if len(mistake_words) < ROUND_WORDS_LIMIT:
            mistake_ids = [word.id for word in mistake_words]

            new_words = self.game_repository.get_new_words(mistake_ids, ROUND_WORDS_LIMIT - len(mistake_words))
            mistake_words.extend(new_words)

        return mistake_words