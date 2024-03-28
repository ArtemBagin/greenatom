from asyncio import current_task
from typing import AsyncGenerator

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_scoped_session, async_sessionmaker
from sqlalchemy.orm import declared_attr, as_declarative

engine = create_async_engine("sqlite+aiosqlite:///database.db", echo=True)
async_session = async_sessionmaker(bind=engine, expire_on_commit=False)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    session = async_scoped_session(async_session, scopefunc=current_task)
    try:
        yield session
    finally:
        await session.remove()


@as_declarative()
class Base:
    @classmethod
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()