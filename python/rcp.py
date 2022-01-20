from network import NetworkServerTCP
from domain import from_json

def transmission_complete(byte_string):
    # create book 
    book = from_json(byte_string)
    print(book)


if __name__ == '__main__':
    srv = NetworkServerTCP('', 20_001, transmission_complete)