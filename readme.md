# BBC News Scraping Project

## Project Overview

This project involves scraping articles from [BBC News](https://www.bbc.com/news), storing them in MongoDB and Neo4j databases, and creating an API using FastAPI to access this data.

## Project Steps


1. **Scraping Articles**:
   - Utilizing BeautifulSoup to extract articles from the BBC News website.
   - Collecting data such as title, sub_title, topics, content, author, and publication date during scraping.
   - The scraping code is located in the file `services/scraping_service.py`.


2. **Data Storage**:
   - Storing scraped data in both MongoDB and Neo4j databases.
   - Both databases are launched from Docker images.
    ![image](https://github.com/amine1956/bbc_scraping/assets/73759527/b1fa7f89-9acc-459f-8f1a-76806e0a5ee3)
    ![image](https://github.com/amine1956/bbc_scraping/assets/73759527/086467c4-92eb-4739-b8eb-e35a4b88f897)

3. **API Creation with FastAPI**:
   - Developing a RESTful API using FastAPI to enable access to stored articles.
   - Implementing endpoints for:
     - Retrieving all articles stored in MongoDB or Neo4j.
     - Obtaining the count of articles per author from BBC News.
     - Identifying the top 20 discussed topics on BBC News.
     ![image](https://github.com/amine1956/bbc_scraping/assets/73759527/2048452e-44b5-4b06-b0ad-7e08d1f9730a)

4. **Data Visualization with JavaScript**:
   - After implementing the API endpoints, data was consumed using JavaScript's `fetch` API to retrieve the stored data.
   - Chart.js was utilized for creating interactive charts and visualizations, including both bar charts and pie charts.
   - The retrieved data was processed and used to populate these types of charts, with bar charts representing certain data distributions and pie charts providing insights into categorical data.
     ![image](https://github.com/amine1956/bbc_scraping/assets/73759527/4bdeca1d-f483-4176-aa8e-7b8c8b9e44ef)




