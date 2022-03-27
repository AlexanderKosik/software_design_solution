import sys
sys.path.append('../domain')

from json_validator import JSONValidator
from book import Book
import jsonschema
import pytest
import json

valid_json = b'{\n   "title": "The Pragmatic Programmer: Your Journey To Mastery, 20th Anniversary Edition",\n   "author": "David Thomas; Andrew Hunt",\n   "isbn-10": "0135957052",\n   "quality": "very good",\n   "language": "english",\n   "publication_date": "2019/09/13",\n   "type": "hardcover",\n "purchase_price": 14.50\n}\n'

# language is missing
invalid_json = b'{\n   "title": "The Pragmatic Programmer: Your Journey To Mastery, 20th Anniversary Edition",\n   "author": "David Thomas; Andrew Hunt",\n   "isbn-10": "0135957052",\n   "quality": "very good",\n "publication_date": "2019/09/13",\n   "type": "hardcover",\n "purchase_price": 14.50\n}\n'

def test_create_book_from_valid_bytes():
    # from_json raises no exception
    Book.from_json(valid_json)

def test_create_book_from_invalid_bytes():
    # from_json raises exception
    invalid_bytes = valid_json[:10]
    with pytest.raises(json.decoder.JSONDecodeError):
        Book.from_json(invalid_bytes)

def test_validator_with_valid_book():
    validator = JSONValidator('../json_book.schema')
    book = Book.from_json(valid_json)
    validator.validate(book)

def test_validator_with_invalid_book():
    j = JSONValidator('../json_book.schema')
    book = Book.from_json(invalid_json)
    with pytest.raises(jsonschema.exceptions.ValidationError):
        j.validate(book)

