from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.api.dependencies import get_db
from app.services.words_service import WordsService

router = APIRouter(prefix="/api/words", tags=["words"])


@router.get('/')
def get_words_list(
    offset: int = Query(
        0, min_value=0, description="Сдвиг (сколько слов пропустить)"),
    page_size: int = Query(50, min_value=1, max_value=200,
                           description="Количество слов на странице"),
    database_session: Session = Depends(get_db)
):
    words_service = WordsService(database_session)
    words_list = words_service.get_all_words(offset, page_size)

    return {
        'items': words_list,
        'count': len(words_list)
    }
