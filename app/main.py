from fastapi import FastAPI
from app.services.news_service import get_news
from typing import List
from app.schemas.news import Article

app = FastAPI()


@app.get('/')
def home():
    return {'message':'News Summarizer'}


@app.get('/news',response_model=List[Article])
async def news(topic: str):
    data = await get_news(topic)

    return data