from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = "sqlite+aiosqlite:///./carteira.db"
db = create_async_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(bind=db, class_=AsyncSession, expire_on_commit=False)