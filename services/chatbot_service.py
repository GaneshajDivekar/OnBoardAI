import os
import requests
from dotenv import load_dotenv

load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# Use the latest Mistral API endpoint
MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"


async def get_mistral_response(message: str):
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "mistral-small",  # Update model as needed
        "messages": [{"role": "user", "content": message}]
    }

    response = requests.post(MISTRAL_API_URL, json=payload, headers=headers)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.json()}"
