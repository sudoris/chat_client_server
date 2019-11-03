from socket import *

serverPort = 12000
# create socket object
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
print(f'Server listening on port: {serverPort}.')
serverName = 'R2'

while True: 
    connectionSocket, addr = serverSocket.accept()      
    clientName = connectionSocket.recv(1024).decode()  
    connectionSocket.send(f'{serverName}'.encode())
    print(f'{clientName} has connected.')   

    while True:     
      msg = connectionSocket.recv(1024).decode()   

      if msg == '\quit':    
          print(f'{clientName} has disconnected')                
          break
      else: 
          print(f'{clientName}: {msg}')
          response = input(f'{serverName}: ')          
          connectionSocket.send(response.encode())     

          if response == '\quit':     
              print(f'Closing connection with {clientName}')         
              break

    connectionSocket.close()

    
     