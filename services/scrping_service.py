from dotenv import load_dotenv
load_dotenv()
from bs4 import BeautifulSoup
import requests

import json
from datetime import datetime

from models.articles_model import Article
from services.mongo_service import insert_many_articles
from services.neo4j_service import init_driver_neo4j, add_article

import os


class BBCScraper:
    def __init__(self, base_url=os.getenv("BBC_URL")):
        self.base_url = base_url

    def fetch_page(self, url):
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
        else:
            response.raise_for_status()

    def parse_json_data(self, html_content):
        soup = BeautifulSoup(html_content, "html.parser")
        script_tag = soup.find('script', id="__NEXT_DATA__")
        if script_tag:
            json_data = json.loads(script_tag.string)
            return json_data['props']['pageProps']['page']['@"news",']['sections']
        else:
            raise ValueError("JSON data not found in the page")

    def get_articles(self):
        html_content = self.fetch_page(self.base_url+"/news")
        sections = self.parse_json_data(html_content)
        articles = []
        for section in sections:
            try:
                for article_content in section["content"]:
                    if "/news/" in article_content["href"]:
                        articles.append(article_content["href"])
            except KeyError:
                print("")
        return articles

    def convert_timestamp_to_datetime(self, timestamp):
        return datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')

    def get_article_details(self, article_url):
        html_content = self.fetch_page(article_url)
        soup = BeautifulSoup(html_content, "html.parser")
        script_tag = soup.find('script', id="__NEXT_DATA__")
        if not script_tag:
            raise ValueError("JSON data not found in the page")

        json_data = json.loads(script_tag.string)['props']['pageProps']["page"]
        key_content_article = list(json_data.keys())[0]
        data_article = json_data[key_content_article]

        sub_title = data_article['contents'][4]['model']['blocks'][0]['model']['text']

        content_data = data_article['contents'][5:]
        content = ""
        for data in content_data:
            try:
                content += data['model']['blocks'][0]['model']['text'] + "\n"
            except KeyError:
                print("No text in this block")

        topics = [x['title'] for x in data_article['topics']]

        json_data = soup.find('script', type="application/ld+json").string
        json_data = json.loads(json_data)

        article1 = {
            "sub_title": sub_title,
            "content": content,
            "topics": topics,
            "title": json_data["headline"],
            "autore": json_data["author"][0]["name"],
            "image": json_data["image"]["url"],
            "data_published": json_data["datePublished"]
        }
        return article1
    def isnert_to_mongo_db(self,data):
        return insert_many_articles(articles_data=data)

    def inser_to_neo4j(self,data):
        driver = init_driver_neo4j()
        with driver.session() as session:
            for article in data:
                session.write_transaction(add_article, article)


if __name__ == "__main__":
    scraper = BBCScraper()

    # Get the list of articles
    articles = scraper.get_articles()

    # Example to get details of a specific article
    data = []
    url = scraper.base_url
    print(url)
    for article in articles:
        try:

            article_details = scraper.get_article_details(url+ article)

            article = Article(
                title=article_details['title'],
                sub_title=article_details['sub_title'],
                content=article_details['content'],
                topics=article_details['topics'],
                author=article_details['autore'],
                image=article_details['image'],
                date_published=article_details['data_published']
            )
            data.append(article)
        except Exception as e:
            print("Error:", e)

    # insert data into data bases
    scraper.isnert_to_mongo_db(data)
    scraper.inser_to_neo4j(data)






