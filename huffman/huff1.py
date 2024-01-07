from collections import Counter  
import heapq
from typing import Union


class HuffmanTree:
    def __init__(self, char: Union[str, None], freq: int):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None
            
    def __lt__(self, other):
        return self.freq < other.freq


def build_tree(data: str):
    frequency = Counter(data)
    
    priority_queue = []
    for char, freq in frequency.items():
        node = HuffmanTree(char, freq);
        priority_queue.append(node)
        
    heapq.heapify(priority_queue)
    
    
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged_node = HuffmanTree(None, left.freq + right.freq)
        merged_node.left = left
        merged_node.right = right
        heapq.heappush(priority_queue, merged_node)
        
    return priority_queue[0]
    
def get_codes(root, current_code = ""):
    huffman_codes = {}
    if root.char is not None:
        huffman_codes[root.char] = current_code
    if root.left is not None:
        huffman_codes.update(get_codes(root.left, current_code + "0"))
    if root.right is not None:
        huffman_codes.update(get_codes(root.right, current_code + "1"))
    return huffman_codes
    

def encode(data):
    root = build_tree(data)
    codes = get_codes(root)
    encoded_data = ''
    for char in data:
        encoded_data += codes[char]
    return encoded_data, codes
    
def decode(encoded_data, codes):
    decoded_data = ""
    current_code = ""
    
    for bit in encoded_data:
        current_code += bit
        for char, code in codes.items():  # <--------CODES.ITEMS()----------->
            if code == current_code:
                decoded_data += char
                current_code = ""
                break
    return decoded_data

def main():
    message = "hello"
    encoded_message, codes = encode(message);
    print(encoded_message)
    decoded_data = decode(encoded_message, codes)
    print(decoded_data)
    
main()