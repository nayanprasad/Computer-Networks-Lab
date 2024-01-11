import string
import random

def binary_mapping():
    return {chr(i): bin(i)[2:] for i in range(48, 123)}

def create_mapping():
  # alphabet = list(string.ascii_uppercase) # ['A', 'B', 'C', ...]
  # shuffled = alphabet.copy()
  # random.shuffle(shuffled)
  # mapping = dict(zip(alphabet, shuffled))  # {'A': 'X', 'B': 'Y', ...}
  # return mapping
  cap = string.ascii_uppercase
  small = string.ascii_lowercase
                                                                              
  result = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9' ]

  for i in range(26):
      result.append(cap[i])
      result.append(small[i])

  shuffled = result.copy()
  random.shuffle(shuffled)
  dicttionary = dict(zip(result, shuffled))

  return dicttionary
  
    
def encrypt(message, cipher_mapping):
  result = []
  b_map = binary_mapping()
  # print(b_map)
  for char in message:
    # if char.isalpha():
      is_upper = char.isupper()
      substituted_char = cipher_mapping.get( char)
      result.append(b_map[substituted_char])
      # result += substituted_char if is_upper else substituted_char.lower()
    # else:
      # result.append(char)
  return result

def decrypt(message, cipher_mapping):
  # inverted_mapping = {v: k for k, v in cipher_mapping.items()}
  # return encrypt(message, inverted_mapping)
  b_map = {bin(i)[2:] : chr(i)  for i in range(48, 123)}
  result = ""
  for i in message:
    print(i)
    char = b_map[i]
    for j in cipher_mapping:
      if cipher_mapping[j] == char:
        result += j
  return result    
        
    
  
def main():
  cipher_mapping = create_mapping()
  message = "2asf"
  
  print(cipher_mapping)
  
  encrypted_message = encrypt(message, cipher_mapping)
  print(encrypted_message)
  
  decrypted_message = decrypt(encrypted_message, cipher_mapping)
  print(decrypted_message)
  
main()