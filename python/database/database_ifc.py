"""
A formal interface for database objects
"""

from abc import ABC, abstractclassmethod

class DBIfc(ABC):
    @abstractclassmethod
    def store(self, book):
        """
        Store the passed book in a database
        """
    
    # @abstractclassmethod
    def all_books(self):
        """
        Returns a list of all available books
        """

