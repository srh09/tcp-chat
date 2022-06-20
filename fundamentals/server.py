import socket

HOST = '192.168.0.18'  # Could use localhost
PORT = 9090  # Avoid using a well known port

def start_listening():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # This socket is just for accepting connections
    server.bind((HOST, PORT))

    server.listen(5)  # if more than 5 connections are waiting then reject

    while True:
        communication_socket, address = server.accept()
        print(f'connected to {address}')
        # the value of bufsize should be a relatively small power of 2, for example, 4096
        message = communication_socket.recv(1024).decode('utf-8')
        print(f'message from client is: {message}')
        communication_socket.send('message received'.encode('utf-8'))
        communication_socket.close()
        print(f'connection with {address} ended')


if __name__ == '__main__':
    start_listening()
