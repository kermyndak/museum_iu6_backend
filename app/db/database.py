from collections.abc import AsyncGenerator
from contextlib import asynccontextmanager
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs


URL_DATABASE = "postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_async_engine(URL_DATABASE)

SessionLocal = async_sessionmaker(autoflush=False, autocommit=False, bind=engine)

# @asynccontextmanager
# async def get_session() -> AsyncGenerator[AsyncSession, None]:
#     async with SessionLocal() as session:
#         yield session

class Base(AsyncAttrs, DeclarativeBase):
    pass
