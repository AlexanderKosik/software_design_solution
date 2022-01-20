import json
from .book import Book

def from_json(byte_string):
    d = json.loads(byte_string)
    b = Book()
    for key, value in d.items():
        setattr(b, key, value)
    return b

