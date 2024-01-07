import socket
import json
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "127.0.0.1"
port = 8008

client_socket.connect((host, port))

user = input("Enter a name: ")

def recieve_message():
  while True:
    recieve_message = client_socket.recv(1024).decode('utf-8')
    json_data = json.loads(recieve_message)
    user = json_data["user"]
    message = json_data["message"]
    print(f"\n{user}: {message}\n")

recieve_tread = threading.Thread(target=recieve_message)
recieve_tread.start()

while True:
  message = input("Enter a message to send to the server (or 'q' to quit): ")
  
  if(message == "q"):
    break
  
  data = {
    "message": message,
    "user": user
  }

  json_data = json.dumps(data)
  
  client_socket.send(json_data.encode('utf-8'))
  
client_socket.close()
  