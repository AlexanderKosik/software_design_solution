class Book:
    """
    This class represents a book.

    All attributes are set in the converter functions.
    It only provides some utility methods like repr and str
    """
    def __str__(self):
        r = "Book:\n"
        for key, value in vars(self).items():
            r += f"{key}: {value}\n"
        return r
