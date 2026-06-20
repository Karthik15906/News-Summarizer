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

    '''incase of nework failure like newsapi is down then it could 
    throw a exception to handle it we use try and except'''

    try :
        async with httpx.AsyncClient() as client:
            # actual API call.
            response = await client.get(url,params=params)
    except Exception:
        raise HTTPException(
            status_code=500, # http status code = 500 = internal server error
            detail = 'unable to connect to news api'
        )

    if response.status_code==401:
        # http status code = 401 = Unauthorized
        raise HTTPException(
            status_code=401,
            detail='Invalid api key'
        )
    # handles cases which are not ok http status code = 200 = ok
    if response.status_code!=200:
        raise HTTPException(
            status_code=response.status_code,
            detail='Failed to fetch news'
        )

    # Converts JSON into a Python dictionary.
    data = response.json()

    articles = data['articles']

    # if no article is returned then the artcles list is empty to handle 
    # http status code = 404 = not found
    if not articles:
        raise HTTPException(
            status_code=404,
            detail='No article found'
        )

    result = []
    for article in articles:
        result.append(
            {
                'title' : article['title']
            }
        )

    return result

async def get_news_text(topic: str):
    
    articles = await get_news(topic)

    combined_text = ""

    for article in articles[:3]:

        combined_text += f"""
        Title : {article['title']}
        """
    return combined_text