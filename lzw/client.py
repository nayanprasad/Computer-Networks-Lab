import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host = "localhost"
port = 6000

client_socket.connect((host, port));

def compress(data):
  dictionary = {chr(i): i for i in range(256)}
  next_code = 256
  result = []
  current = ""
  
  for symbol in data:
    current += symbol
    if current not in dictionary:
      dictionary[next_code] = current
      next_code += 1
      result.append(dictionary[current[0:-1]])
      current = symbol
      
  if current in dictionary:
    result.append(dictionary[current])

  return result      
  

def main():
  message = input("Enter a message: ");
  compressed_message = compress(message)
  client_socket.send(str(compressed_message).encode())
  client_socket.close()
  
  
main()