import select
import socket
HOST = '127.0.0.1'  # Standard loopback interface address (localhost)
PORT = 52472        # Port to listen on (non-privileged ports are > 1023)

def send_all(clients, msg):
    for client in clients:
        client.send(msg.encode())

def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # create TCP socket
    s.bind((HOST, PORT)) # bind the socket with the IP and the port
    s.listen() # open the socket for client connections
    print("waiting for clients...")
    clients = {}
    while True:
        rlist, _, _= select.select([s]+[*clients], [], [], 0.1)
        if(len(rlist))>0:
            for sock in rlist:
                if sock == s:
                    new_Client, _ = s.accept()  # wait until client will connect
                    clients[new_Client] = new_Client.recv(1024).decode()
                else:
                    data = sock.recv(1024).decode()
                    data = clients[sock] + ": " + data
                    send_all(clients, data)
main()