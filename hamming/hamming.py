def hamming_encode(data):
    # Calculate the number of parity bits required
    r = 0
    while 2 ** r < len(data) + r + 1:
        r += 1

    # Initialize the encoded message with parity bits set to 0
    encoded_data = [0] * (len(data) + r)
    j = 0

    # Fill in data bits
    for i in range(1, len(encoded_data) + 1):
        if i & (i - 1) == 0:
            continue  # Skip parity bit positions
        encoded_data[i - 1] = int(data[j])
        j += 1

    # Fill in parity bits
    for i in range(r):
        position = 2 ** i
        parity = 0
        for j in range(1, len(encoded_data) + 1):
            if j & position != 0:
                parity ^= encoded_data[j - 1]
        encoded_data[position - 1] = parity

    return encoded_data


def hamming_decode(encoded_data):
    # Calculate the number of parity bits required
    r = 0
    while 2 ** r < len(encoded_data):
        r += 1

    # Initialize the syndrome
    syndrome = [0] * r  # syndrome is the error position

    # Calculate syndrome bits
    for i in range(r):
        position = 2 ** i
        for j in range(1, len(encoded_data) + 1):
            if j & position != 0:
                syndrome[i] ^= encoded_data[j - 1]

    # Check for errors
    error_position = sum([2 ** i * syndrome[i] for i in range(r)]) # convert syndrome to decimal

    if error_position != 0:
        print("Error detected at position:", error_position)
        # Correct the error
        encoded_data[error_position - 1] ^= 1

    # Extract and return the original data
    decoded_data = [encoded_data[i] for i in range(len(encoded_data)) if i & (i + 1) != 0] 
    return decoded_data


def main():
    # data = input("Enter 4 bits of data: ")
    data = "1011010"
    # if len(data) != 4 or not all(bit in '01' for bit in data):
    #     print("Invalid input. Please enter 4 bits of binary data.")
    #     return

    encoded_data = hamming_encode(data)
    print("Encoded data:", encoded_data)

    decoded_data = hamming_decode(encoded_data)
    print("Decoded data:", decoded_data)


main()
