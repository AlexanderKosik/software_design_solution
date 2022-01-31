from fastapi import FastAPI
from database import SQLDatabase

app = FastAPI()
db = SQLDatabase()

@app.get("/")
async def root():
    content = "".join(str(book) for book in db.all_books())
    return {"message": content}
