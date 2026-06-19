from dotenv import load_dotenv
import httpx
from fastapi import HTTPException
import os

load_dotenv()

API_KEY = os.getenv('News_api_key')

async def get_news(topic : str):
    url = "https://newsapi.org/v2/everything"

    # Query parameters.
    params = {
        'q': topic,
        'apikey':API_KEY
    }
    async with httpx.AsyncClient() as client:
        # actual API call.
        response = await client.get(url,params=params)

    # handles cases which are not ok http code = 200 = ok
    if response.status_code!=200:
        raise HTTPException(
            status_code=response.status_code,
            detail='Failed to fetch news'
        )

    # Converts JSON into a Python dictionary.
    data = response.json()

    articles = data['articles']

    # if no article is returned then the artcles list is empty to handle 
    # http code = 404 = not found
    if not articles:
        raise HTTPException(
            status_code=404,
            detail='No article found'
        )

    result = []
    for article in articles:
        result.append(
            {
                'title' : article['title'],
                'description' : article['description'],
                'url' : article['url']
            }
        )

    return result