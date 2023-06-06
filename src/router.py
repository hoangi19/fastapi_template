from fastapi.routing import APIRouter
from src import docs, user

api_router = APIRouter()
api_router.include_router(docs.router)
api_router.include_router(user.router)