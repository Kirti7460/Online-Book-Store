import os

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./bookstore.db"

# Create the engine and database connection
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create the base model for SQLAlchemy
Base = declarative_base()

# Create the database tables
def create_tables():
    from .models import Book  # Import your models here
    Base.metadata.create_all(bind=engine)

# Generate a new database file
def generate_database():
    if os.path.exists(SQLALCHEMY_DATABASE_URL):
        os.remove(SQLALCHEMY_DATABASE_URL)
    create_tables()
