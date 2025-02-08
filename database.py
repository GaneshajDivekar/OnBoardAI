import os
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncSession
from sqlalchemy.orm import declarative_base
from dotenv import load_dotenv

# ✅ Load environment variables (for local testing)
load_dotenv()

# ✅ Get DATABASE_URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("🚨 DATABASE_URL is not set! Check your environment variables.")

# ✅ Create async SQLAlchemy engine
engine = create_async_engine(DATABASE_URL, echo=True, future=True)

# ✅ Define Base for ORM models
Base = declarative_base()

# ✅ Create async session factory
async_session_maker = async_sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)

# ✅ Dependency to get the database session
async def get_db():
    async with async_session_maker() as session:
        yield session
