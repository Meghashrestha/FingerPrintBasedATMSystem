# pip install sockets
# pip install jupyter
# jupyter notebook
# This is the UDPClient file/program

from socket import *
serverName = '127.0.0.1'#local machine IP: 127.0.0.1
serverPort = 12000
# create UDP socket for server
clientSocket = socket(AF_INET, SOCK_DGRAM)
# take input from user's keyboard
message=input("Client: Input lowercase sentence:")
# send it to server through the socket
clientSocket.sendto(message.encode(),(serverName, serverPort))

# wait and receive the reply from the server
modifiedMessage,serverAddress=clientSocket.recvfrom(2048)
# modifiedMessage is a bytes object
print("Client:", modifiedMessage.decode())
print("Client:",serverAddress)
clientSocket.close()

