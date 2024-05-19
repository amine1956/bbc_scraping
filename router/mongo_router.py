from fastapi import (
    APIRouter
)

from services.mongo_service import get_articles

mongo_router = APIRouter(
    prefix='/mongo',
    tags=['db_mongo']
)


@mongo_router.get("/get_all_articles")
def get_all_articles_from_mongo():
    return get_articles()

