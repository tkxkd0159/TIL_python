import socket as sc

clientSocket = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
clientSocket.connect(('127.0.0.1', 8080))

print("connection is successful")
clientSocket.send("I am a client".encode('utf-8'))
print("Send message")

data = clientSocket.recv(1024)  # get 1024 bytes
print("received data : ", data.decode('utf-8'))