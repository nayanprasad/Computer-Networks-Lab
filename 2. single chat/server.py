import socket
import threading
import json

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "localhost"
port = 8008

server_socket.bind((host, port))
server_socket.listen(5)

print("listening...")

connected_clients = []

def handleClient(client_socket):
  global connected_clients
  while True:
    data = client_socket.recv(1024).decode('utf-8')
    if not data:
      break
    
    message = json.loads(data)
    user = message["user"]
    content = message["message"]
    
    print(f"{user}: {content}")
    
    for client in connected_clients:
      if client != client_socket:
        client.send(data.encode('utf-8'))
  

while 1:
  client_socket, addr = server_socket.accept()
  print(f"connetion  from {addr}")
  
  connected_clients.append(client_socket)  
  clinet_handler = threading.Thread(target=handleClient, args=(client_socket,))
  clinet_handler.start()
  
