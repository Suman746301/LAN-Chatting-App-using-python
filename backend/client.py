#client.py
#client.py
import socket
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "172.16.185.179" # "127.0.1.1"
port = 8000
my_socket.connect((host, port))
while True:
    message_to_send = input("Enter your message : ")
    my_socket.send(message_to_send.encode())
