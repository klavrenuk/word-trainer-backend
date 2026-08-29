from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.database import engine, Base

from app.models import user
from app.models import word
from app.models import user_mistake
from app.models import user_results

from app.api.routes import profile
from app.api.routes import auth
from app.api.routes import words
from app.api.routes import game
from app.api.routes import admin
from app.api.routes import users
from app.api.routes import statistics

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(profile.router)
app.include_router(auth.router)
app.include_router(words.router)
app.include_router(game.router)
app.include_router(admin.router)
app.include_router(users.router)
app.include_router(statistics.router)

@app.get("/")
def start():
    return {"message": "Trainer words"}
