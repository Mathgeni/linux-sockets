import os
import socket

SOCKET_FILE = './server.socket'

if os.path.exists(SOCKET_FILE):
    os.remove(SOCKET_FILE)

print("Открываем UNIX сокет...")
server = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
server.bind(SOCKET_FILE)

print("Слушаем...")
while True:
    data = server.recv(1024)
    if not data:
        break
    data = data.decode('utf-8')
    if data == 'close':
        break
    print(data)
print('Closing')
server.close()
os.remove(SOCKET_FILE)
