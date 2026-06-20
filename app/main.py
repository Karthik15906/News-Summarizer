from fastapi import FastAPI
from app.services.news_service import get_news_text, get_news
from typing import List
from app.schemas.news import Article
from app.services.gemini_service import summarizer
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware ,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

@app.get('/')
def home():
    return {'message':'News Summarizer'}


@app.get('/news',response_model=List[Article])
async def news(topic: str):
    data = await get_news(topic)

    return data

@app.get('/test-gemini')
async def test_gemini():

    summary = await summarizer(
         "OpenAI released a new reasoning model with improved coding capabilities."
    )

    return {
        'summary': summary
    }

@app.get('/news-summary')
async def news_summary(topic : str):

    news_text = await get_news_text(topic)
    summary = await summarizer(news_text)
    return {
        'topic':topic,
        'summary':summary,
    }