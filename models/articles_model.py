from pydantic import BaseModel, Field
from typing import List
from datetime import date


class Article(BaseModel):
    title: str = Field(..., title="Title of the article")
    sub_title: str = Field(..., title="Subtitle of the article")
    content: str = Field(..., title="Content of the article")
    topics: List[str] = Field(..., title="List of topics related to the article")
    author: str = Field(..., title="Author of the article")
    image: str = Field(..., title="Path to the image associated with the article")
    date_published: str = Field(..., title="Publication date of the article")