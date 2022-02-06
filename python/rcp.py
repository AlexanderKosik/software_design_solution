from network import NetworkServerTCP
from configparser import ConfigParser
from domain import Book

from database import SQLDatabase
db = SQLDatabase()

# from database import MongoDatabase
# db = MongoDatabase()

def transmission_complete(byte_string):
    # create book 
    book = Book.from_json(byte_string)

    # log receiving of book
    print(book)

    db.store(book)


if __name__ == '__main__':
    cfg = ConfigParser()
    cfg.read('config.ini')
    port = cfg.getint('server', 'port')
    ip = cfg.get('server', 'ip')

    srv = NetworkServerTCP(ip, port, transmission_complete)
