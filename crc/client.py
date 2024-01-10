import socket

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = "localhost"
PORT = 8000
KEY = "1001"


client_socket.connect((HOST, PORT))

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
			cipher = xor(cipher, "0" * cipher_len) + data[cipher_len]
		cipher_len += 1
	
	if cipher[0] == "1":
		cipher = xor(cipher, KEY)
	else:
		cipher = xor(cipher, "0" * cipher_len)
	return cipher

def encrypt(message):
		l = len(KEY)
		appended_data = message + "0" * (l - 1)
		remainder = mod2div(appended_data) 
		return message + remainder
	

def main():
	message = input("enter the message: ")
	encrypted_message = encrypt(message)
	client_socket.send(encrypted_message.encode())
	
main()
