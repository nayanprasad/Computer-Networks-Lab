import socket


client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)


server_address = ('localhost', 8080)

while True:
    
    message = input("Enter a message to send to the server (or 'quit' to exit): ")
    
    if message.lower() == 'quit':
        break

    
    client_socket.sendto(message.encode(), server_address)

    
    data, server_address = client_socket.recvfrom(1024)
    print("Server response:", data.decode())


client_socket.close()
