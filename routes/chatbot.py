from fastapi import APIRouter
from pydantic import BaseModel
from services.chatbot_service import get_mistral_response

router = APIRouter()

# ✅ Define request schema
class ChatRequest(BaseModel):
    message: str

# ✅ Async route for chatbot response
@router.post("/chat/")
async def chat(request: ChatRequest):
    response = await get_mistral_response(request.message)
    return {"response": response}
