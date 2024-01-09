KEY = "1001"


def xor(a, b):
    result = []
    for i in range(1, len(a)):
        if a[i] == b[i]:
            result.append("0")
        else:
            result.append("1")
    return "".join(result)  # eg: result = ['0', '1', '0', '1'] -> "0101"


def mod2div(data):
    cipher_len = len(KEY)
    cipher = data[0:cipher_len]

    while cipher_len < len(data):
        if cipher[0] == "1":  # if MSB is 1
            cipher = xor(cipher, KEY) + data[cipher_len] # xor with key and append next bit
        else:
            cipher = xor(cipher, "0" * cipher_len) + data[cipher_len] # xor with 0 and append next bit
        cipher_len += 1

    if cipher[0] == "1":
        cipher = xor(cipher, KEY)
    else:
        cipher = xor(cipher, "0" * cipher_len)
    return cipher


def encrypt(data):
    l_key = len(KEY)
    appended_data = data + "0" * (l_key - 1)
    remainder = mod2div(appended_data)	
    codeword = data + remainder
    return codeword


def decrypt(data):
    l_key = len(KEY)
    appended_data = data + "0" * (l_key - 1)
    remainder = mod2div(appended_data)
    return remainder


def main():
    # data = input()
    data = "10"

    encrypt_message = encrypt(data)
    print("Encrypted message: ", encrypt_message)

    remainder = decrypt(encrypt_message)
    print("Remainder:", remainder)

    check = "0" * (len(KEY) - 1)

    if remainder == check:
        print("No error found in data")
    else:
        print("Error found in data")


main()




'''
algorithms:
1. input data
2. append 0s to data
3. divide data by key
'''