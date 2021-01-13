import socket
import time
import threading

HOST = "127.0.0.1"
PORT = 52472    # Port to listen on (non-privileged ports are > 1023)
def check_for_new_data(s):
    while True:
        data = s.recv(1024).decode()
        print(data)

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((HOST, PORT))
    x = threading.Thread(target=check_for_new_data, args=(s,))
    x.start()
    name = input("enter your name: ")
    s.send(name.encode()) # send hello after converting it to bytes
    while True:
        data = input()
        s.send(data.encode())

    #s.close()

main()