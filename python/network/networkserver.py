from socketserver import TCPServer
from .handlerfactory import handler_factory

class NetworkServerTCP:
    """
    This class is a TCP Network Server listening on passed ip and port

    It can receive files and calls the passed callback if the file transfer 
    is completed
    """
    def __init__(self, ip, port, callback):
        self.serv = TCPServer((ip, port), handler_factory(callback))
        print(f"Listening on {ip}:{port}")
        self.serv.serve_forever()