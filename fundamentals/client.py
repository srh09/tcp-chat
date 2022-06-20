import socket

HOST = '192.168.0.18'
PORT = 9090


def connect_and_send():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    client.connect((HOST, PORT))

    client.send('hello socket server'.encode('utf-8'))
    print(client.recv(1024).decode('utf-8'))

if __name__ == '__main__':
    connect_and_send()
