from socketserver import BaseRequestHandler

class TCPHandler(BaseRequestHandler):
    def __init__(self, callback, *args, **kwargs):
        """
        When a new connection arrives the callback is called with the payload
        """
        self._callback = callback
        super().__init__(*args, **kwargs)

    def handle(self):
        print('Got connection from', self.client_address)
        msg = b''
        while True:
            new_block = self.request.recv(8192)
            msg += new_block
            # if we have no more data, we are finished
            if not new_block:
                break
        
        # call callback with the received message
        self._callback(msg)
