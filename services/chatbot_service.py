import os
from mistralai.client import MistralClient
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()
MISTRAL_API_KEY = os.getenv("MISTRAL_API_KEY")

# ✅ Initialize MistralClient
client = MistralClient(api_key=MISTRAL_API_KEY)


# ✅ Correct function: No `await` on `client.chat(...)`
async def get_mistral_response(message: str):
    chat_messages = [{"role": "user", "content": message}]

    # ❌ Do NOT use `await` here, since `client.chat(...)` is synchronous
    response = client.chat(model="mistral-tiny", messages=chat_messages)

    # ✅ Extract message content correctly
    return response.choices[0].message.content
