import socket


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


server_address = ('localhost', 8080)


server_socket.bind(server_address)

print("Server is listening on", server_address)

while True:
   
    data, client_address = server_socket.recvfrom(1024)
    
    
    message = data.decode()
    
    print("Received message from", client_address, ":", message)

    
    server_socket.sendto(data, client_address)

