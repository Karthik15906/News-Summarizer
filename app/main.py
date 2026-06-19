from fastapi import FastAPI
from app.services.news_service import get_news

app = FastAPI()


@app.get('/')
def home():
    return {'message':'News Summarizer'}


@app.get('/news')
async def news(topic: str):
    data = await get_news(topic)

    return data