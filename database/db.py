from asyncio import current_task

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, async_scoped_session, AsyncSession

from .db_config import db_config


class Base(DeclarativeBase):
    pass


class DataBaseHelper:
    def __init__(self, url: str, echo: bool = False):
        self.engine = create_async_engine(
            url=url,
            echo=echo
        )
        self.session_factory = async_sessionmaker(
            bind=self.engine,
            autoflush=False,
            autocommit=False,
            expire_on_commit=False
        )

    def get_scoped_session(self):
        session = async_scoped_session(
            session_factory=self.session_factory,
            scopefunc=current_task,
        )
        return session

    async def get_session(self) -> AsyncSession:
        async with self.get_scoped_session() as session:
            yield session
            await session.remove()


db_helper = DataBaseHelper(
    url=db_config.DB_URL,
    echo=db_config.BD_ECHO
)