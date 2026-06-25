import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

_db_path = os.environ.get("DB_PATH", "/tmp/trusted.db")
DATABASE_URL = f"sqlite:///{_db_path}"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def init_db():
    Base.metadata.create_all(bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
