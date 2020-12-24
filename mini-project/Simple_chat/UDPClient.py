# AF_INET : indicates IPv4, SOCK_DGRM : indicates that it is a UDP socket
# AF : Address Family
import socket as sc

serverName = 'hostname'
serverPort = 12000
clientSocket = sc.socket(sc.AF_INET, sc.SOCK_DGRAM)
message = input('Input lowercase sentence:')  # 무조건 string 입력. 따라서 int나 float 입력할 땐 int(), float()으로 형변환 해줘야 됨
clientSocket.sendto(message.encode(), (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)
print(modifiedMessage.decode())
clientSocket.close()