
from typing import List
from pymongo import MongoClient
import os
from models.articles_model import Article
def get_database():
    client = MongoClient(os.getenv("MONGODB_URI"))
    return client['your_database_name']

def insert_article(article_data: Article):
    db = get_database()
    collection = db['articles']
    result = collection.insert_one(article_data.dict())
    return str(result.inserted_id)

def insert_many_articles(articles_data: List[Article]):
    db = get_database()
    collection = db['articles']
    result = collection.insert_many([article.dict() for article in articles_data])
    return [str(id) for id in result.inserted_ids]

def get_articles(query: dict = {}):
    db = get_database()
    collection = db['articles']
    articles = collection.find(query)
    return [Article(**article) for article in articles]