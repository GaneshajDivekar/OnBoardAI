from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from database import create_tables
import models
from routes import onboarding, chatbot

# ✅ Initialize FastAPI app
app = FastAPI()

# ✅ CORS Middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# ✅ FastAPI Startup Event - Auto Create Tables
@app.on_event("startup")
async def startup_event():
    """Ensure database tables are created on startup."""
    await create_tables()  # ✅ Auto-create tables in PostgreSQL

# ✅ Include API Routes
app.include_router(onboarding.router, prefix="/api")
app.include_router(chatbot.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "AI-Powered Onboarding Chatbot is Running"}
