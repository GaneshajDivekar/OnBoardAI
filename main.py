import asyncio
from fastapi import FastAPI
from database import engine
import models
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

# ✅ Correctly initialize the async database
async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

# Run the database initialization
@app.on_event("startup")
async def startup_event():
    await init_db()

# ✅ Include API routes
app.include_router(documents.router, prefix="/api")
app.include_router(training.router, prefix="/api")
app.include_router(chatbot.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "AI-Powered Onboarding Chatbot is Running"}
