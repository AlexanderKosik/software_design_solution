from network import NetworkServerTCP
from domain import from_json
from configparser import ConfigParser

def transmission_complete(byte_string):
    # create book 
    book = from_json(byte_string)
    print(book)


if __name__ == '__main__':
    cfg = ConfigParser()
    cfg.read('config.ini')
    port = cfg.getint('server', 'port')
    ip = cfg.get('server', 'ip')

    srv = NetworkServerTCP(ip, port, transmission_complete)