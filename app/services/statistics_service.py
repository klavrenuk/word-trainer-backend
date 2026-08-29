from sqlalchemy.orm import Session

from app.repositories.statistics_repository import StatisticsRepository

class StatisticsService:
    def __init__(self, db: Session):
        self.db = db
        self.statistics_repository = StatisticsRepository(db)
        
    def get_mistakes_words(self, user_id: int):
        return self.statistics_repository.get_user_mistakes(user_id)

    def get_learned_words(self, user_id:int):
        return self.statistics_repository.get_user_learned_words(user_id)

    def get_user_statistics(self, user_id:int):
        mistakes = self.get_mistakes_words(user_id)
        learned = self.get_learned_words(user_id)

        return {
            'mistakes': len(mistakes),
            'learned': len(learned)
        }