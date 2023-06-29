from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from sqlalchemy import create_engine, Column, Integer, String, Float, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database
from datetime import datetime
from pydantic import BaseModel

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:8000"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE"],
    allow_headers=["*"],
)


# Mount the static files directory
app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure the database connection
SQLALCHEMY_DATABASE_URL = "sqlite:///./bookstore.db"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)
database = Database(SQLALCHEMY_DATABASE_URL)

# Create the base model for SQLAlchemy
Base = declarative_base()

# Models
class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), nullable=False)
    author = Column(String(255), nullable=False)
    description = Column(Text, nullable=False)
    price = Column(Float, nullable=False)
    rating = Column(Float, nullable=True)
    cover_image = Column(String(255), nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

class BookCreate(BaseModel):
    title: str
    author: str
    description: str
    price: float

# Routes
@app.on_event("startup")
async def startup():
    await database.connect()

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

@app.get("/")
async def index():
    return FileResponse("static/index.html")

@app.get("/books")
async def get_books():
    query = Book.__table__.select()
    result = await database.fetch_all(query)
    return result

@app.post("/books")
async def create_book(book: BookCreate):
    query = Book.__table__.insert().values(**book.dict())
    await database.execute(query)
    return {"message": "Book created successfully"}

# Run the FastAPI application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
