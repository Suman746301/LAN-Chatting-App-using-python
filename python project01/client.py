#client.py
#client.py
import socket
import threading
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "localhost" # "127.0.1.1"
port = 8000
my_socket.connect((host, port))


def thread_receiving():
    while True:
        message = my_socket.recv(1024).decode()
        print("message received: ", message)
        
        
def thread_sending():
    while True:
        message_to_send = input()
        my_socket.send(message_to_send.encode())


thread_send = threading.Thread(target=thread_sending)
thread_receive = threading.Thread(target=thread_receiving)

thread_receive.start()
thread_send.start()
          




                                    