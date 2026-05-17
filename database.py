"""
Database Connection and Session Management
Async SQLAlchemy 2 with asyncpg
"""
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import (
    create_async_engine,
    AsyncSession,
    async_sessionmaker,
)
from sqlalchemy.pool import NullPool

import structlog

from app.core.config import settings

logger = structlog.get_logger(__name__)

# Engine instance
engine = None
async_session_maker = None


async def init_db() -> None:
    """Initialize database connection pool and create tables."""
    global engine, async_session_maker
    
    engine = create_async_engine(
        settings.DATABASE_URL,
        echo=settings.DB_ECHO,
        pool_size=settings.DB_POOL_SIZE,
        max_overflow=settings.DB_MAX_OVERFLOW,
        pool_recycle=settings.DB_POOL_RECYCLE,
        pool_pre_ping=True,
        poolclass=NullPool if settings.ENVIRONMENT == "testing" else None,
    )
    
    async_session_maker = async_sessionmaker(
        engine,
        class_=AsyncSession,
        expire_on_commit=False,
        autoflush=False,
    )
    
    # Create tables (in production, use Alembic migrations)
    async with engine.begin() as conn:
        # await conn.run_sync(Base.metadata.create_all)
        pass
    
    logger.info("Database initialized", url=settings.DATABASE_URL)


async def close_db() -> None:
    """Close database connection pool."""
    global engine
    if engine:
        await engine.dispose()
        logger.info("Database connection closed")


async def get_session() -> AsyncGenerator[AsyncSession, None]:
    """Get database session for dependency injection."""
    if not async_session_maker:
        raise RuntimeError("Database not initialized")
    
    async with async_session_maker() as session:
        try:
            yield session
        except Exception as e:
            await session.rollback()
            logger.error("Database session error", error=str(e))
            raise
        finally:
            await session.close()