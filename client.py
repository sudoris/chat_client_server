from socket import *

serverIP = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientName = input('Enter your username: ')
clientSocket.connect((serverIP, serverPort))
clientSocket.send(clientName.encode())
serverName = clientSocket.recv(1024).decode()
print(f'You have connected to {serverName}.')

while True:
  msg = input(f'{clientName}: ') 
  clientSocket.send(msg.encode())
  if msg == '\quit':
      print(f'Closing connection with {serverName}.')
      break
  serverResponse = clientSocket.recv(1024).decode()
  if serverResponse == '\quit':
      print(f'Connection closed by {serverName}.')
      break
  else:
      print(f'{serverName}:', serverResponse)  

clientSocket.close()

