import os
from mistralai.client import MistralClient
from dotenv import load_dotenv

load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

client = MistralClient(api_key=MISTRAL_API_KEY)

async def get_mistral_response(message: str):
    chat_messages = [{"role": "user", "content": message}]
    response = client.chat(model="mistral-tiny", messages=chat_messages)
    return response.choices[0].message["content"]
