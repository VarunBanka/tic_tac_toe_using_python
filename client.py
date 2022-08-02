import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
SERVER = "192.168.0.16"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

"""send("Hello World!")
input()
send("Hello Everyone!")
input()
send("Hello Tim!")"""
while True:
    x = client.recv(2048).decode(FORMAT)
    print(x, x == "Your turn", type(x))
