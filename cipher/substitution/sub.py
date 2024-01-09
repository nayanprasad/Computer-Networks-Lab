import string

def substitution_cipher(text, key):
    result = ""

    for char in text:
        if char.isalpha():
            case_offset = ord('A') if char.isupper() else ord('a')
            encrypt_char = chr(((ord(char) - case_offset + key) % 26) + case_offset)
            result += encrypt_char
        else:
            result += char

    return result

def main():
    original_text = "Hello, World!"
    substitution_key = 3

    encrypted_text = substitution_cipher(original_text, substitution_key)

    print("Original Text:", original_text)
    print("Encrypted Text:", encrypted_text)

if __name__ == "__main__":
    main()
