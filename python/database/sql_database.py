from sqlalchemy import create_engine, MetaData
from sqlalchemy.orm import Session, sessionmaker
from .db_book import Book
from .database_ifc import DBIfc

class SQLDatabase(DBIfc):
    def __init__(self):
        # self.engine = create_engine("sqlite:///rcp.db", echo=True)
        self.engine = create_engine("sqlite://", echo=True)
        self.Session = sessionmaker(bind=self.engine)

        # create tables 
        Book.__table__.create(bind=self.engine, checkfirst=True)

    def store(self, book):
        session = self.Session()

        db_book = Book()
        db_book.content = book.json
        session.add(db_book)
        session.commit()
