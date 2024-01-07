import socket 

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = socket.gethostname()
port = 5003

client_socket.connect((host, port))

while True:
  message = input()
  
  if message == 'q':
    break

  client_socket.send(message.encode('utf-8'))
  
client_socket.close()