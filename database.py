from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import asyncio
import os
from dotenv import load_dotenv

# ✅ Load environment variables (for local testing)
load_dotenv()

# ✅ Get DATABASE_URL from Railway
DATABASE_URL = os.getenv("DATABASE_URL")

if not DATABASE_URL:
    raise ValueError("🚨 DATABASE_URL is not set! Check your Railway environment variables.")

# ✅ Create async SQLAlchemy engine
engine = create_async_engine(DATABASE_URL, future=True, echo=True)

# ✅ Define Base for models
Base = declarative_base()

# ✅ Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, class_=AsyncSession)

# ✅ Database Connection Retry (Fix TimeoutError)
async def test_connection():
    """Check if the database connection is successful."""
    for attempt in range(5):  # Retry 5 times
        try:
            async with engine.begin() as conn:
                await conn.run_sync(Base.metadata.create_all)
            print("✅ Database connection successful!")
            return
        except Exception as e:
            print(f"⚠️ Database connection failed (Attempt {attempt + 1}/5): {e}")
            await asyncio.sleep(5)  # Wait 5 seconds before retrying

    print("❌ Database connection failed after multiple attempts.")
    raise Exception("Database connection failed after multiple retries.")

# ✅ Ensure connection before app starts
asyncio.run(test_connection())

# ✅ Dependency to get the database session
async def get_db():
    async with SessionLocal() as session:
        yield session
