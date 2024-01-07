import socket 

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

host = socket.gethostname()
port = 5003

server_socket.bind((host, port))
server_socket.listen(5) 

print(f"listening on {host}:{port}")


while True:
  client_socket, addr = server_socket.accept()
  print(f"connection from {addr}")
  
  message = client_socket.recv(1024).decode()
  print(message)
  
  client_socket.close()
