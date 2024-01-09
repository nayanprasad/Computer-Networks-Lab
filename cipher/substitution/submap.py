import string
import random

def create_mapping():
  alphabet = list(string.ascii_uppercase) # ['A', 'B', 'C', ...]
  shuffled = alphabet.copy()
  random.shuffle(shuffled)
  mapping = dict(zip(alphabet, shuffled))  # {'A': 'X', 'B': 'Y', ...}
  return mapping
  
    
def encrypt(message, cipher_mapping):
  result = ""
  for char in message:
    if char.isalpha():
      is_upper = char.isupper()
      substituted_char = cipher_mapping.get(char.upper(), char)
      result += substituted_char if is_upper else substituted_char.lower()
    else:
      result += char
  return result

def decrypt(message, cipher_mapping):
  inverted_mapping = {v: k for k, v in cipher_mapping.items()}
  return encrypt(message, inverted_mapping)
  
  
def main():
  cipher_mapping = create_mapping()
  message = "HELLO world"
  
  print(cipher_mapping)
  
  encrypted_message = encrypt(message, cipher_mapping)
  print(encrypted_message)
  
  decrypted_message = decrypt(encrypted_message, cipher_mapping)
  print(decrypted_message)
  
main()