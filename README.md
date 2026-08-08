# Word Trainer Backend

API для приложения по изучению английских слов.

## Технологии

- Python 3.14
- FastAPI
- SQLAlchemy
- SQLite
- JWT авторизация
- bcrypt для хеширования паролей

## Установка

```bash
git clone <url>
cd word-trainer-backend

# Создай и активируй виртуальное окружение:
python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # Mac/Linux

# Установи зависимости:
pip install -r requirements.txt

# Настрой базу данных:
alembic upgrade head

# Загрузи слова в базу:
python seed_words.py

# Запуск сервера:
uvicorn app.main:app --reload
```

## Установка
```bash
app/
├── api/ # Обработка запросов
│   ├── routes/
│   └── dependencies.py   # Внедрение зависимостей
│
├── services/   # Бизнес-логика
│
├── repositories/  # Доступ к данным
│
├── models/  # Описание таблиц
│
├── schemas/  # Валидация данных
│
├── core/  # Настройки и база
│   ├── config.py
│   ├── database.py
│   └── exceptions.py
│
└── main.py
```