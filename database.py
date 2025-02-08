from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# ✅ Get the PostgreSQL URL from Railway environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("🚨 DATABASE_URL is not set! Check your Railway environment variables.")

# ✅ Create async SQLAlchemy engine
engine = create_async_engine(DATABASE_URL, future=True, echo=True)

# ✅ Define Base for models
Base = declarative_base()

# ✅ Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

# ✅ Dependency to get the database session
async def get_db():
    async with SessionLocal() as session:
        yield session
