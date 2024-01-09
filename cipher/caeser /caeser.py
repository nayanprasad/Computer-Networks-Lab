
def encrypt(data, shift):
  result = ""
  
  for char in data:
    if char.isalpha():
      case_offset = ord('A') if char.isupper() else ord('a')
      encrypt_char = chr(((ord(char) - case_offset + shift) % 26) + case_offset)
      result += encrypt_char
  
  return result

def decrypt(data, shift):
  result = ""
  
  for char in data:
    if char.isalpha():
      case_offset = ord('A') if char.isupper() else ord('a')
      decrypt_char = chr(((ord(char) - case_offset - shift) % 26) + case_offset)
      result += decrypt_char
  
  return result


def main():
  message = "hello"
  shift = 3
  
  print(encrypt(message, shift))
  print(decrypt(encrypt(message, shift), shift))
  
  
main()