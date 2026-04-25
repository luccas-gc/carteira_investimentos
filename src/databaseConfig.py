from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import declarative_base, sessionmaker
import os

DATABASE_URL = os.getenv("DATABASE_URL")
db = create_async_engine(DATABASE_URL)
Base = declarative_base()
SessionLocal = sessionmaker(bind=db, class_=AsyncSession, expire_on_commit=False)