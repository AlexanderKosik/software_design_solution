from .networkhandler import TCPHandler

def handler_factory(callback):
    """
    A TCPServer needs a callable for every request.
    Since our TCPHandler needs a callback, we have this handler_factory
    which will pass our callback to the TCPHandler
    """
    def create_handler(*args, **kwargs):
        return TCPHandler(callback, *args, **kwargs)
    return create_handler