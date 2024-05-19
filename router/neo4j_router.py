from fastapi import (
    APIRouter
)

from services.neo4j_service import get_all_articles, init_driver_neo4j

neo4j_router = APIRouter(
    prefix='/neo4j',
    tags=['db_neo4j']
)


@neo4j_router.get("/get_all_articles")
def get_all_articles_from_neo4j():
    driver = init_driver_neo4j()
    with driver.session() as session:
        all_articles = session.read_transaction(get_all_articles)
    return all_articles