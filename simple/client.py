import socket
import threading

HOST = '192.168.0.18'  # localhost
PORT = 9090
BUFSIZE = 1024  # Small power of 2

def receive(nickname: str):
    while True:
        try:
            message = client.recv(BUFSIZE).decode('utf-8')
            if message == 'NICK':
                client.send(nickname.encode('utf-8'))
                continue
            print(message)
        except:
            print('An error occurred.  Disconnecting.')
            client.close()
            break

def write(nickname: str):
    while True:
        message = f'{nickname}: {input("")}'
        client.send(message.encode('utf-8'))

if __name__ == '__main__':
    nickname = input('Choose a nickname: ')
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((HOST, PORT))
    receive_thread = threading.Thread(target=receive, args=(nickname,))
    write_thread = threading.Thread(target=write, args=(nickname,))
    receive_thread.start()
    write_thread.start()
