import socket
import threading

# Threading is when one piece of code runs at a different time
# Purpose of threads is not to delay other clients to handle another one

# We're defining a fixed length header such that the first message sent
# every time such that the message has to be 64 bytes, one of these numbers says the length of the message
HEADER = 64
# We need a port where data runs to
PORT = 5050
# This code gets the IP address automatically for us
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (server,PORT)
DISCONNECT_MSG = "!Disconnect"
# This essentially creates a socket and AF_INET tells it the kind of
# Addresses we are excepting
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

FORMAT = 'utf-8'
# This means that anything that hits this sockets address is bound to this port which is 5050
sever.bind(ADDR)

# This handles threads
def handle_client(conn,addr):
    print(f"New connection {addr} connected")
    connected = True
    while connected:
        # This decodes the message format into a string which is the messages length
        msg_length = conn.recv(HEADER).decode(FORMAT)
        msg_length = int(msg_length)
        msg = conn.recv(msg_length).decode(FORMAT)
        print(f"[{msg}]")
    
        # we need to handle disconnect
        if msg == DISCONNECT_MSG:
            connected = FALSE
    
    conn.close()
def start():
    # This makes our server always listen for messages to address
    server.listen()

    #Always runs while true
    while True:

        # This waits for a new connection to the server
        # IT stores IP address and port it came from
        # conn is a socket object that lets us communicate back to it
        conn, addr = server.accept()

        # This will execute the function in a new thread, handle client
        # It will pass the arguments conn and address
        thread = threading.Thread(target=handle_client, args=(conn,addr))
        thread.start()

        # this tells us the amount of clients active which each has a thread
        # Start thread is an extra so we - it away
        print(f"Active connections {threading.active_count() - 1}")

print("[Starting] server is starting...")
start()