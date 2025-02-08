from fastapi import APIRouter
from services.chatbot_service import get_response
from schemas import ChatRequest

router = APIRouter()


@router.post("/chat/")
async def chat(request: ChatRequest):
    response = await get_response(request.message)
    return {"response": response}

