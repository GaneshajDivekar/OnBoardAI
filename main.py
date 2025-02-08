import os
import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import engine
import models

# ✅ Use Railway's DATABASE_URL environment variable
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("🚨 DATABASE_URL is not set! Check your Railway environment variables.")

# ✅ Lifespan event handling (Replaces @app.on_event("startup"))
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Starting up: Initializing database...")
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    yield
    print("🛑 Shutting down: Closing database connections...")

# ✅ Initialize FastAPI with lifespan
app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"message": "AI-Powered Onboarding Chatbot is Running"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Use Railway's assigned port
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
    #true
