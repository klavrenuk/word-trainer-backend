from sqlalchemy.orm import Session
from app.models.user_mistake import UserMistake
from app.repositories.game_repository import GameRepository

class GameService:
    def __init__(self, db:Session):
        self.db = db
        self.game_repository = GameRepository(db)
        
    def finish_round(self, user_id: int, answers: list):
        mistake_ids = []
        for answer in answers:
            mistake_ids.append(answer.id)

        print(mistake_ids)
        if mistake_ids:
            self.game_repository.add_mistakes(user_id, mistake_ids)


    def start_round(self, user_id: int, count_words:int):
        mistake_words = self.game_repository.get_mistake_words(user_id, count_words)

        if len(mistake_words) < count_words:
            mistake_ids = [word.id for word in mistake_words]

            new_words = self.game_repository.get_new_words(mistake_ids, count_words - len(mistake_words))
            mistake_words.extend(new_words)

        return mistake_words