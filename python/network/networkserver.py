from socketserver import TCPServer
from .handlerfactory import handler_factory

class NetworkServerTCP:
    def __init__(self, ip, port, callback):
        self.serv = TCPServer((ip, port), handler_factory(callback))
        self.serv.serve_forever()