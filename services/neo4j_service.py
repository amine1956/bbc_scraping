from neo4j import GraphDatabase
from models.articles_model import Article
import os

def add_article(tx, article: Article):
    tx.run(
        """
        CREATE (n:Article {
            title: $title, 
            sub_title: $sub_title, 
            content: $content, 
            topics: $topics, 
            author: $author, 
            image: $image, 
            date_published: $date_published
        })
        """,
        title=article.title,
        sub_title=article.sub_title,
        content=article.content,
        topics=article.topics,
        author=article.author,
        image=article.image,
        date_published=article.date_published
    )

def init_driver_neo4j():
    driver = GraphDatabase.driver(os.getenv("NEO4J_DRIVER"),auth=(os.getenv("NEO4J_USER"),os.getenv("NEO4J_PASSWORD")))
    return driver


def get_all_articles(tx):
    result = tx.run("MATCH (n:Article) RETURN n")
    return [record["n"] for record in result]


def get_articles_by_topic(tx, topic: str):
    result = tx.run(
        """
        MATCH (n:Article) 
        WHERE $topic IN n.topics 
        RETURN n
        """,
        topic=topic
    )
    return [record["n"] for record in result]


def get_articles_by_author(tx, author: str):
    result = tx.run(
        """
        MATCH (n:Article) 
        WHERE n.author = $author 
        RETURN n
        """,
        author=author
    )
    return [record["n"] for record in result]