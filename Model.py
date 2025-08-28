from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), '..', '.env'))

def respond(query: str, max_tokens=1000):
    client = OpenAI(api_key=os.getenv("OpenAI"))

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=query,
        max_tokens=max_tokens
    )

    return response.choices[0].message.content