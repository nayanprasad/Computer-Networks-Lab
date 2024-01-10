import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "localhost"
PORT = 8000
KEY = "1001"


server_socket.bind((HOST, PORT))
server_socket.listen(5)
print(f"server listening...")

def xor(a, b):
	result = ""
	for i in range(1, len(a)):
		if a[i] == b[i]:
			result += "0"
		else:
			result += "1"
	return result

def mod2div(data):
	cipher_len = len(KEY)
	cipher = data[0:cipher_len]
	
	while cipher_len < len(data):
		if cipher[0] == "1":
			cipher = xor(cipher, KEY) + data[cipher_len]
		else:
			cipher = xor(cipher, "0" * len(KEY)) + data[cipher_len]
		cipher_len += 1;
		
	if cipher[0] == "1":
		cipher = xor(cipher, KEY)
	else:
		cipher = xor(cipher, "0" * len(KEY)) 
	
	return cipher

def decrypt(data):
	append_data = data + "0" * (len(KEY) - 1)
	remainder = mod2div(append_data)
	
	check = "0" * (len(KEY) - 1)
	is_error = True
	
	if check == remainder:
		is_error = False
		
		
	return data[0:len(data) - len(KEY) + 1], is_error
	
	
while True:
	client_socket, addr = server_socket.accept()
	print(f"connected {addr}")
	
	message = client_socket.recv(1024).decode()
	
	decrypted_message, is_error = decrypt(message)
	
	if(is_error):
		print("error")
	else:
		print(decrypted_message)
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	
