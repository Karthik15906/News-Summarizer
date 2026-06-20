from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

genai.configure(api_key=GEMINI_API_KEY)

model = genai.GenerativeModel('gemini-2.5-flash')

async def summarizer(text: str):
    prompt = f"""
    You are a professional news analysts.
    Analyze the following news articles.
    provide: Executive mini summary
    keep the response concise
    Articles:

    {text}
    """

    response = model.generate_content(prompt)
    # model.generate_content(prompt) returns a response object, not a plain string
    
    return response.text # extracting only the generated text and returning it as a normal Python string.