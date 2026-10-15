from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Books API")


class BookCreate(BaseModel):
    title: str
    author: str


books = [
    {"id": 1, "title": "The Hobbit", "author": "J.R.R. Tolkien"},
    {"id": 2, "title": "A Wrinkle in Time", "author": "Madeleine L'Engle"},
]


@app.get("/")
def read_root():
    return {"message": "Books API is running"}


# Add GET, POST, and PUT endpoints for the assignment here.
