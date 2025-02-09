import os
import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager
from database import engine
import models
from routes import documents, training, chatbot
from fastapi.middleware.cors import CORSMiddleware

# ✅ Get PORT from environment variables (default to 8000)
PORT = int(os.getenv("PORT", 8000))

# ✅ Use lifespan for proper async database initialization
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("🚀 Starting up: Initializing database...")
    async with engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)
    yield
    print("🛑 Shutting down: Closing database connections...")

# ✅ Initialize FastAPI with lifespan
app = FastAPI(lifespan=lifespan)

# ✅ Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to limit origins in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ Include API routes
app.include_router(documents.router, prefix="/api")
app.include_router(training.router, prefix="/api")
app.include_router(chatbot.router, prefix="/api")

@app.get("/")
async def read_root():
    return {"message": "AI-Powered Onboarding Chatbot is Running 🚀"}

# ✅ Run Uvicorn Server Properly (For Render)
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=PORT, reload=True)
