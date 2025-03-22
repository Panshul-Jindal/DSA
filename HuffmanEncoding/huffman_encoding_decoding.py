import heapq
from collections import Counter, namedtuple

class HuffmanNode(namedtuple("HuffmanNode", ["char", "freq", "left", "right"])):
    def __lt__(self, other):
        return self.freq < other.freq
    


# class HuffmanNode:
#     def __init__(self, char, freq, left=None, right=None):
#         self.char = char
#         self.freq = freq
#         self.left = left
#         self.right = right
    
#     def __lt__(self, other):
#         return self.freq < other.freq


def build_huffman_tree(text):
    freq_map = Counter(text)
    priority_queue = [HuffmanNode(char, freq, None, None) for char, freq in freq_map.items()]
    heapq.heapify(priority_queue)
    
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        merged = HuffmanNode(None, left.freq + right.freq, left, right)
        heapq.heappush(priority_queue, merged)
    
    return priority_queue[0] if priority_queue else None

def generate_huffman_codes(root, prefix="", code_map={}):
    if root is not None:
        if root.char is not None:
            code_map[root.char] = prefix
        generate_huffman_codes(root.left, prefix + "0", code_map)
        generate_huffman_codes(root.right, prefix + "1", code_map)
    return code_map

def huffman_encode(text, code_map):
    return "".join(code_map[char] for char in text)

def huffman_decode(encoded_text, root):
    decoded_text = ""
    current = root
    for bit in encoded_text:
        current = current.left if bit == "0" else current.right
        if current.char is not None:
            decoded_text += current.char
            current = root
    return decoded_text

if __name__ == "__main__":
    text = "this is an example of huffman encoding"
    root = build_huffman_tree(text)
    huffman_codes = generate_huffman_codes(root)
    encoded_text = huffman_encode(text, huffman_codes)
    decoded_text = huffman_decode(encoded_text, root)
    
    print("Original Text:", text)
    print("Huffman Codes:", huffman_codes)
    print("Encoded Text:", encoded_text)
    print("Decoded Text:", decoded_text)



## Done using AI
