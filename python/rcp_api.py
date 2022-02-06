from fastapi import FastAPI
from database import SQLDatabase
from domain import Book
import json

app = FastAPI()
db = SQLDatabase()

@app.get("/books/")
async def books(author: str = "", title: str = "", limit: int = 100):
    return {'books': db.all_books()}

@app.get("/all_books/")
async def all_books(limit: int = 100):
    return {'books': db.all_books(limit)}
