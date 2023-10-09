import os
import socket

SOCKET_FILE = './server.socket'

if os.path.exists(SOCKET_FILE):
    client = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    client.connect(SOCKET_FILE)
    print('Connected')
    while True:
        message = input('data: ')
        client.send(message.encode('utf-8'))
        if message == 'close':
            break
    client.close()
