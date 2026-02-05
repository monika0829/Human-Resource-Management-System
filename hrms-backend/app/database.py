import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# 1. This looks for a variable named "DATABASE_URL" in Render's settings.
# 2. If it doesn't find it (like on your local PC), it defaults to your local database.
DATABASE_URL = os.getenv(
    "DATABASE_URL", 
    "postgresql://postgres:123@localhost/HRMS_DB"
)

# Render and other providers sometimes use 'postgres://', 
# but SQLAlchemy 2.0+ requires 'postgresql://'
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()