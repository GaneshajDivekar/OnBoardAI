from fastapi import APIRouter
from schemas import ChatRequest
from services.chatbot_service import get_mistral_response

router = APIRouter()


@router.post("/chat/")
async def chat(request: ChatRequest):
    response = await get_mistral_response(request.message)
    return {"response": response}
