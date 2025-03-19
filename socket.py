import socket

# every time such that the message has to be 64 bytes, one of these numbers says the length of the message
HEADER = 64
# We need a port where data runs to
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MSG = "!Disconnect"
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER, PORT)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)