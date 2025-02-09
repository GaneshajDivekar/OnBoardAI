import asyncio
from logging.config import fileConfig
from sqlalchemy.ext.asyncio import AsyncEngine
from alembic import context
from database import engine  # ✅ Import Async Engine
from models import Base  # ✅ Import ORM models

# ✅ Alembic Config
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ✅ Metadata from ORM models
target_metadata = Base.metadata


async def run_migrations_online():
    """Run migrations using an async engine."""
    async with engine.begin() as conn:
        await conn.run_sync(lambda sync_conn: context.configure(connection=sync_conn, target_metadata=target_metadata))
        await conn.run_sync(lambda sync_conn: context.run_migrations())  # ✅ FIXED SYNTAX!


def run():
    """Run Alembic migrations asynchronously."""
    asyncio.run(run_migrations_online())  # ✅ Ensuring proper async execution


run()
