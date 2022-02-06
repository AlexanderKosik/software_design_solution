import json

class Book:
    """
    This class represents a book.

    All attributes are set in the converter functions.
    It only provides some utility methods like repr and str
    """

    @classmethod
    def from_json(cls, byte_string):
        d = json.loads(byte_string)
        self = cls()
        for key, value in d.items():
            setattr(self, key, value)
        self._json = byte_string
        return self

    @classmethod
    def from_database(cls, db_book):
        return cls.from_json(db_book.content)

    def __str__(self):
        r = "Book:\n"
        for key, value in vars(self).items():
            r += f"{key}: {value}\n"
        return r

    def __repr__(self):
        return f"Book({dir(self)})"
