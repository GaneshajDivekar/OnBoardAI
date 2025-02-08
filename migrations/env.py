from logging.config import fileConfig
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from alembic import context
import models  # ✅ Ensure models are imported so Alembic detects them
from database import Base, DATABASE_URL  # ✅ Import Base from database.py
from sqlalchemy.ext.asyncio import create_async_engine

# ✅ Configure Alembic Logging
config = context.config
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ✅ Set up the correct database URL for async PostgreSQL
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# ✅ Set target metadata for Alembic migrations
target_metadata = Base.metadata

# ✅ Create async engine for database migrations
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

def run_migrations_online():
    """Run migrations in 'online' mode using async engine."""
    connectable = create_async_engine(DATABASE_URL, future=True, echo=True)

    with connectable.connect() as connection:  # ✅ Use sync context manager
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
        )
        with context.begin_transaction():
            context.run_migrations()

# ✅ Determine which mode to run: offline or online
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
