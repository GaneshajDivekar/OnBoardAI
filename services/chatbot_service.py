import os
import requests
from dotenv import load_dotenv

load_dotenv()

MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

MISTRAL_API_URL = "https://api.mistral.ai/v1/chat/completions"
DEEPSEEK_API_URL = "https://api.deepseek.ai/v1/chat/completions"  # Update with actual DeepSeek endpoint if different


def get_deepseek_response(message: str):
    headers = {
        "Authorization": f"Bearer {DEEPSEEK_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "deepseek-chat",  # Update with actual DeepSeek model name
        "messages": [{"role": "user", "content": message}]
    }
    try:
        response = requests.post(DEEPSEEK_API_URL, json=payload, headers=headers)
        if response.status_code == 200:
            print("Getting response from DeepSeek model")
            return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"DeepSeek API Error: {e}")
    return None


def get_mistral_response(message: str):
    headers = {
        "Authorization": f"Bearer {MISTRAL_API_KEY}",
        "Content-Type": "application/json"
    }
    payload = {
        "model": "mistral-small",  # Update with actual Mistral model name if needed
        "messages": [{"role": "user", "content": message}]
    }
    try:
        response = requests.post(MISTRAL_API_URL, json=payload, headers=headers)
        if response.status_code == 200:
            print("Getting response from Mistral model")
            return response.json()["choices"][0]["message"]["content"]
    except Exception as e:
        print(f"Mistral API Error: {e}")
    return "Failed to get a response from both DeepSeek and Mistral."


def get_response(message: str):
    response = get_deepseek_response(message)
    if response:
        return response
    return get_mistral_response(message)
