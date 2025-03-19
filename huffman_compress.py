# Implementation of Huffman Encoding Code & Byte Conversion 
# Resources: https://www.geeksforgeeks.org/huffman-coding-in-python/
#            https://www.programiz.com/dsa/huffman-coding 

import os
import heapq
import pickle

from collections import Counter

from huffman_tree import build_huffman_tree
from huffman_codes import build_codes

# Read input text
file_path = "input.txt"
with open(file_path, "r", encoding="utf-8") as f:
    text = f.read()
 
# Build Huffman Tree & Huffman Codes
freq_map = Counter(text)
huffman_tree = build_huffman_tree(freq_map)
huffman_codes = build_codes(huffman_tree)

# Encode text
encoded_text = "".join(huffman_codes[char] for char in text)

# Pad encoded text for byte storage
def pad_encoded_text(encoded_text):
    padding = (8 - len(encoded_text) % 8) % 8               # calculates how much padding is needed based on multiples of 8
    padded_conversion = format(padding, '08b')              # converting padding length to 8bit binary
    return padded_conversion + encoded_text + '0' * padding # appends padding

def binary_to_bytes(padded_text):
    return bytes(int(padded_text[i:i+8], 2)
                 for i in range(0, len(padded_text), 8))

# Converts encoded text into binary and pads it
padded_text = pad_encoded_text(encoded_text)

# Converts the padded binary string into bytes
compressed_data = binary_to_bytes(padded_text)

# Save the compressed data
with open("compressed.data", "wb") as f:
    f.write(compressed_data)

# Save Huffman Codes for decompressing (later use)
with open("huffman_codes.pkl", "wb") as f:
    pickle.dump(huffman_codes, f)


og_file = os.path.getsize("input.txt")
compressed_file = os.path.getsize("compressed.data")

# Print Messages

print(f"Original: {og_file} bytes")
print(f"Compressed: {compressed_file} bytes")
ratio = 100 - (compressed_file / og_file * 100)
print(f"Ratio: {ratio:.2f}%")