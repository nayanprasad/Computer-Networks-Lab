import heapq  
from collections import Counter # Counter is a dict subclass for counting hashable objects
from typing import Union, Tuple 

class HuffmanNode:
    def __init__(self, char: Union[str, None], freq: int):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other): # less than
        return self.freq < other.freq

def build_huffman_tree(data: str) -> HuffmanNode:
    # Count frequencies of characters in the data
    freq_counter = Counter(data)  

    # Build a priority queue (min heap) for the characters and their frequencies
    # priority_queue = [HuffmanNode(char, freq) for char, freq in freq_counter.items()]    
    priority_queue = []
    for char, freq in freq_counter.items():
        node = HuffmanNode(char, freq)
        priority_queue.append(node)
        

    heapq.heapify(priority_queue) # heapify() converts a regular list to a heap

    # Build the Huffman tree
    while len(priority_queue) > 1:
        left_child = heapq.heappop(priority_queue)
        right_child = heapq.heappop(priority_queue)
        merged_node = HuffmanNode(None, left_child.freq + right_child.freq)
        merged_node.left = left_child
        merged_node.right = right_child
        heapq.heappush(priority_queue, merged_node)

    # The root of the tree is the single node left in the priority queue
    return priority_queue[0]

def build_huffman_codes(node: HuffmanNode, current_code: str = "") -> dict:
    huffman_codes = {}
    if node.char is not None:
        huffman_codes[node.char] = current_code
    if node.left is not None:
        huffman_codes.update(build_huffman_codes(node.left, current_code + "0"))
    if node.right is not None:
        huffman_codes.update(build_huffman_codes(node.right, current_code + "1"))
    return huffman_codes

def huffman_encode(data: str) -> Tuple[dict, str]:
    root = build_huffman_tree(data)
    codes = build_huffman_codes(root)
    encoded_data = ''
    for char in data:
        encoded_data += codes[char]    
    return codes, encoded_data

def huffman_decode(encoded_data: str, codes: dict) -> str:
    decoded_data = ""
    current_code = ""
    for bit in encoded_data:
        current_code += bit
        for char, code in codes.items():
            if current_code == code:
                decoded_data += char
                current_code = ""
                break
    return decoded_data

def main():
    message = "hello"
    
    # Encode the message using Huffman coding
    huffman_codes, encoded_message = huffman_encode(message)
    print("Original Message:", message)
    print("Encoded Message:", encoded_message)
    print("Huffman Codes:", huffman_codes)
    
    # Decode the encoded message
    decoded_message = huffman_decode(encoded_message, huffman_codes)
    print("Decoded Message:", decoded_message)

if __name__ == "__main__":
    main()
