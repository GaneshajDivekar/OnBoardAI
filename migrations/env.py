from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from alembic import context
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine
from database import Base, DATABASE_URL  # ✅ Import Base from database.py
import models  # ✅ Import models to detect schema changes

# ✅ Configure Alembic Logging
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ✅ Set the correct database URL
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# ✅ Set target metadata for Alembic migrations
target_metadata = Base.metadata

# ✅ Create async engine for database migrations
connectable = create_async_engine(DATABASE_URL, future=True, echo=True)


async def run_migrations_online():
    """Run migrations in 'online' mode using async engine."""
    async with connectable.begin() as connection:
        await connection.run_sync(context.configure, connection=connection, target_metadata=target_metadata)
        await connection.run_sync(context.run_migrations)


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


# ✅ Determine whether to run online or offline migrations
if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())  # ✅ Correct way to handle async migration
