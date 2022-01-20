from network import NetworkServerTCP

def transmission_complete(byte_string):
    print(byte_string)

if __name__ == '__main__':
    srv = NetworkServerTCP('', 20_001, transmission_complete)