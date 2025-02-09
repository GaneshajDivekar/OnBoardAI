import os
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv

# ✅ Load environment variables
load_dotenv()

# ✅ Get DATABASE_URL from Railway or local `.env`
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("🚨 DATABASE_URL is not set! Check your environment variables.")

# ✅ Create Async SQLAlchemy engine
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# ✅ Define Base for ORM models
Base = declarative_base()

# ✅ Create async session factory
async_session_maker = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# ✅ Async function to create tables
async def create_tables():
    """Creates tables asynchronously at startup."""
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

# ✅ Dependency to get the database session
async def get_db():
    async with async_session_maker() as session:
        yield session
