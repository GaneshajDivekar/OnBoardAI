import os
from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Import your models here (for automatic migrations)
from models import Base  # Ensure this import exists

# Configure Alembic logging
config = context.config
fileConfig(config.config_file_name)

# Get the database URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://user:1234@localhost/interviewbot")

# Use `psycopg2` for Alembic migrations (convert asyncpg -> psycopg2)
SYNC_DATABASE_URL = DATABASE_URL.replace("asyncpg", "psycopg2")

# Set the SQLAlchemy URL dynamically
config.set_main_option("sqlalchemy.url", SYNC_DATABASE_URL)

# Metadata for database migrations
target_metadata = Base.metadata  # Ensure models are imported correctly


def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=SYNC_DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = create_engine(
        SYNC_DATABASE_URL,
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
import os
from logging.config import fileConfig
from sqlalchemy import create_engine, pool
from alembic import context
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Convert asyncpg to psycopg2 for Alembic migrations
DATABASE_URL = os.getenv("DATABASE_URL", "postgresql+asyncpg://postgres:1234@localhost/interviewbot")
SYNC_DATABASE_URL = DATABASE_URL.replace("asyncpg", "psycopg2")

# Set database URL for Alembic
config.set_main_option("sqlalchemy.url", SYNC_DATABASE_URL)

# Import models
from models import Base  # Ensure this import exists

# Metadata for migrations
target_metadata = Base.metadata

def run_migrations_offline():
    """Run migrations in 'offline' mode."""
    context.configure(
        url=SYNC_DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        compare_type=True,
    )
    with context.begin_transaction():
        context.run_migrations()

def run_migrations_online():
    """Run migrations in 'online' mode."""
    connectable = create_engine(
        SYNC_DATABASE_URL,
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(
            connection=connection,
            target_metadata=target_metadata,
            compare_type=True,
        )

        with context.begin_transaction():
            context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

