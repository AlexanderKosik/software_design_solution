from fastapi import FastAPI
from database import SQLDatabase
from domain import Book
import json

app = FastAPI()
db = SQLDatabase()

@app.get("/")
async def root():
    books = [Book.from_database(book) for book in db.all_books()]
    payload = [
                json.dumps(
                    {k:v for k,v in book.__dict__.items() if not k.startswith('_')},
                    indent=4
                ) 
                for book in books
            ]
    return {"books": "".join(payload)}
