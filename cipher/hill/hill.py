import numpy as np

def text_to_matrix(text, size):
    text = text.upper().replace(" ", "")
    padding = size - len(text) % size if len(text) % size != 0 else 0
    text += 'X' * padding
    matrix = [ord(char) - 65 for char in text]
    return np.array(matrix).reshape(-1, size)

def matrix_to_text(matrix):
    text = ''.join([chr(int(val) + 65) for val in matrix.flatten()])
    return text
    
def mod_mat_inv(matrix, modulus):
    det = int(np.round(np.linalg.det(matrix)))
    det %= modulus
    det_inv = -1
    for i in range(1, modulus):
        if (det * i) % modulus == 1:
            det_inv = i
            break
    if det_inv == -1:
        raise ValueError("Modular inverse does not exist")
    matrix_modulus_inv = (det_inv * np.round(det * np.linalg.inv(matrix)).astype(int)) % modulus
    return matrix_modulus_inv


def encrypt_message(plain_text, key):
    size = len(key)
    plain_matrix = text_to_matrix(plain_text, size)
    key_matrix = np.array(key)
    encrypted_matrix = np.dot(plain_matrix, key_matrix) % 26
    encrypted_text = matrix_to_text(encrypted_matrix)
    return encrypted_text
    
def decrypt_message(encrypted_text, key):
    size = len(key)
    inverse_key = mod_mat_inv(np.array(key), 26)
    decrypted_matrix = np.dot(text_to_matrix(encrypted_text, size), inverse_key) % 26
    decrypted_text = matrix_to_text(decrypted_matrix)
    return decrypted_text
    
    
def main():
    key = [[3, 2], [5, 7]]  # Replace this with your own 2x2 key matrix
    #message_to_encrypt = input("Enter the message :")  # Replace this with your message
    message_to_encrypt = "hellow"
    
    encrypted_message = encrypt_message(message_to_encrypt, key)
    print("Encrypted message:", encrypted_message)
    
    decrypted = decrypt_message(encrypted_message, key)
    print("Decrypted message:", decrypted)
    
main()
