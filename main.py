from fastapi import FastAPI
from database import test_connection
import asyncio
from routes import documents, training, chatbot
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Use lifespan event instead of asyncio.run()
@app.on_event("startup")
async def startup():
    await test_connection()  # ✅ This will run on FastAPI's event loop

app.include_router(documents.router, prefix="/api")
app.include_router(training.router, prefix="/api")
app.include_router(chatbot.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "AI-Powered Onboarding Chatbot is Running"}
