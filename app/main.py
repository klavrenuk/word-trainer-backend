from fastapi import FastAPI

from app.api.routes import profile
from app.api.routes import auth

app = FastAPI()

app.include_router(profile.router)
app.include_router(auth.router)

@app.get("/")
def hello_world():
    return {"message": "Hello world trainer"}