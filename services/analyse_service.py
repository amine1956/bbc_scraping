import pandas as pd
import json

def get_autthor_and_her_articles_count(articles):
    author_count = {}
    for article in articles:
        author = article['author']
        if author in author_count:
            author_count[author] += 1
        else:
            author_count[author] = 1
    return author_count

def get_top_20_topics(articles, top_n=20):
    topics = []
    for article in articles:
        topics.extend(article['topics'])
    topics = pd.Series(topics)
    top_topics = dict(topics.value_counts().head(top_n))
    print(top_topics)
    top_topics = {k: int(v) for k, v in top_topics.items()}
    return top_topics