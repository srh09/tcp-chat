# Demo given here https://www.youtube.com/watch?v=3UOyky9sEQY

import threading
import socket
from typing import List

HOST = '192.168.0.18'  # localhost
PORT = 9090
BUFSIZE = 1024  # Small power of 2

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

clients: List[socket.socket] = []
nicknames = []

def broadcast(message):
    for client in clients:
        client.send(message)

def handle(client: socket.socket):  # This handles receiving a message from a client and broadcasting to all clients on the chat.
    while True:
        try:
            message = client.recv(BUFSIZE)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f'{nickname} left the chat'.encode('utf-8'))
            nicknames.remove(nickname)
            break

def receive():  # This handles receiving new clients to the chat
    while True:
        client, address = server.accept()
        print(f'Connected with {address}')

        client.send('NICK'.encode('utf-8'))  # Prompt the client to send the nickname
        nickname = client.recv(BUFSIZE).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f'Nickname of the client is {nickname}')
        broadcast(f'{nickname} joined the chat!'.encode('utf-8'))
        client.send('Connected to the server!'.encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))  # Start a thread to handle the connection with this particular client.
        thread.start()

print(f'Server is listening on {HOST}:{PORT}')

if __name__ == '__main__':
    receive()
