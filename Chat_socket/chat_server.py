import socket as sc
serverSocket = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
serverSocket.bind(('', 8080))
serverSocket.listen(1)
connectionSocket, addr = serverSocket.accept()

print(str(addr), 'connect with server')

data = connectionSocket.recv(1024)
print('received data :', data.decode('utf-8'))

connectionSocket.send('reply to client'.encode('utf-8'))
print('Sent a message')