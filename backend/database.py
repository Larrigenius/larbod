import os
from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker, declarative_base

from config import settings

load_dotenv()
DATABASE_URL = os.getenv("DATABASE_URL")

if not all([
    settings.db_user,
    settings.db_password,
    settings.db_host,
    settings.db_port,
    settings.db_name,
]):
    raise RuntimeError("Database configuration is incomplete")


DATABASE_URL = URL.create(
    drivername="postgresql+psycopg2",
    username=settings.db_user,
    password=settings.db_password,
    host=settings.db_host,
    port=int(settings.db_port),
    database=settings.db_name,
)


engine = create_engine(DATABASE_URL)


SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine,
)


Base = declarative_base()
def get_db():
    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()