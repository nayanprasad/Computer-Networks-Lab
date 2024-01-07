import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "localhost"
PORT = 6000

server_socket.bind((HOST, PORT))
server_socket.listen(5)


def decompress(data):
  dictionary = {i: chr(i) for i in range(256)}
  next_code = 256
  result = []
  
  prev_code = data[0]
  result.append(dictionary[prev_code])
  
  for code in data[1:]:
    if code in dictionary:
      entry = dictionary[code]
    elif code == next_code:
      entry = dictionary[prev_code] + dictionary[prev_code][0]
    else:
      raise ValueError("invalid data")
    
    result.append(entry)
    dictionary[next_code] = dictionary[prev_code] + entry[0]
    next_code += 1
    prev_code = code
    
  return ''.join(result)
      

def main():
  client_socket, address = server_socket.accept()
  data = client_socket.recv(1024).decode();
  data = eval(data) # convert string to list
  decompressed_message = decompress(data)
  print(decompressed_message)
  
main()