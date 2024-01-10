def compress(data):
    dictionary = {chr(i): i for i in range(256)}  # eg: {'a': 97, 'b': 98, 'c': 99, 'd': 100}

    next_code = 256
    result = []
    current = ""

    for symbol in data:
        current += symbol
        if current not in dictionary:
            dictionary[current] = next_code
            next_code += 1
            result.append(dictionary[current[:-1]])  # append code of current without last symbol (eg: 'ab' -> 'a')  current[0:-1] = current[:-1] | ie from first to last-1
            current = symbol

    if current in dictionary:
        result.append(dictionary[current])  

    return result


def decompress(compressed_data):
    dictionary = {i: chr(i) for i in range(256)} # eg: {97: 'a', 98: 'b', 99: 'c', 100: 'd'}
    next_code = 256
    result = []

    prev_code = compressed_data[0]
    result.append(dictionary[prev_code])

    for code in compressed_data[1:]:  # start from 2nd element
        if code in dictionary:
            entry = dictionary[code]
        elif code == next_code:
            entry = dictionary[prev_code] + dictionary[prev_code][0] 
        else:
            raise ValueError("Invalid compressed data")

        result.append(entry)
        dictionary[next_code] = dictionary[prev_code] + entry[0]   
        next_code += 1
        prev_code = code

    return ''.join(result)


def main():
    #   message = input("Enter message: ")
    compressed = compress("wabb")
    print("Compressed message: ", compressed)
    decompressed = decompress(compressed)
    print("Decompressed message: ", decompressed)


main()
