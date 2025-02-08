from fastapi import FastAPI
from contextlib import asynccontextmanager
import os
import uvicorn

from database import engine
import models

@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Starting up: Initializing DB")
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    yield
    print("Shutting down: Closing DB connection")

app = FastAPI(lifespan=lifespan)

@app.get("/")
def read_root():
    return {"message": "AI-Powered Onboarding Chatbot is Running"}

if __name__ == "__main__":
    port = int(os.getenv("PORT", 8000))  # Use Railway's assigned port
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
