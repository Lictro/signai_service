from fastapi import APIRouter
from app.api.controllers import router as predict_router

routes = APIRouter()

routes.include_router(predict_router)
