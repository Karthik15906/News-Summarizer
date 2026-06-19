from dotenv import load_dotenv
import httpx
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

    # Converts JSON into a Python dictionary.
    return response.json()