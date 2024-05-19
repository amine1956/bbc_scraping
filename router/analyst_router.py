from fastapi import (
    APIRouter
)

from services.analyse_service import get_autthor_and_her_articles_count, get_top_20_topics
from services.neo4j_service import init_driver_neo4j, get_all_articles

analyst_router = APIRouter(
    prefix='/analyst',
    tags=['analyst']
)

@analyst_router.get("/get_articles_count_per_author")
def get_articles_count_per_author1():
    driver = init_driver_neo4j()
    with driver.session() as session:
        all_articles = session.read_transaction(get_all_articles)

    return get_autthor_and_her_articles_count(all_articles)

@analyst_router.get("/get_top_20_topics")
def get_top_tpics():
    driver = init_driver_neo4j()
    with driver.session() as session:
        all_articles = session.read_transaction(get_all_articles)
    return get_top_20_topics(all_articles)

