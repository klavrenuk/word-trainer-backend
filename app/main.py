from fastapi import FastAPI

from app.api.routes import profile

app = FastAPI()

app.include_router(profile.router)

@app.get("/")
def hello_world():
    return {"message": "Hello world trainer"}