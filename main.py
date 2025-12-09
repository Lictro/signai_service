from fastapi import FastAPI
from app.api.routes import routes

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Hello, SignAI!"}

app.include_router(routes)
