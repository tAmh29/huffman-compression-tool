# Implementation of Huffman Encoding Code & Byte Conversion 
# Resources: https://www.geeksforgeeks.org/huffman-coding-in-python/
#            https://www.programiz.com/dsa/huffman-coding 

import os
import heapq
import pickle

from collections import Counter

from huffman_tree import build_huffman_tree
from huffman_codes import build_codes

# Pad encoded text for byte storage
def pad_encoded_text(encoded_text):
    padding = (8 - len(encoded_text) % 8) % 8               # calculates how much padding is needed based on multiples of 8
    padded_conversion = format(padding, '08b')              # converting padding length to 8bit binary
    return padded_conversion + encoded_text + '0' * padding # appends padding

def binary_to_bytes(padded_text):
    return bytes(int(padded_text[i:i+8], 2)
                 for i in range(0, len(padded_text), 8))

def compress_text(text):
    # Build Huffman Tree & Huffman Codes
    freq_map = Counter(text)
    huffman_tree = build_huffman_tree(freq_map)
    huffman_codes = build_codes(huffman_tree)

    # Encode text
    encoded_text = "".join(huffman_codes[char] for char in text)

    # Pad encoded text for byte storage
    padded_text = pad_encoded_text(encoded_text)

    # Convert the padded binary string into bytes
    compressed_data = binary_to_bytes(padded_text)

    return compressed_data, huffman_codes

def compress_file_to_disk(input_path):
    # Read text from file
    with open(input_path, "r", encoding="utf-8") as f:
        text = f.read()

    # Get compressed data and huffman codes from compress_text function
    compressed_data, huffman_codes = compress_text(text)

    # Generate output paths
    base_path = os.path.splitext(input_path)[0]
    bin_path = base_path + "_compressed.bin"
    pkl_path = base_path + "_codes.pkl"

    # Save files
    with open(bin_path, "wb") as f:
        f.write(compressed_data)

    with open(pkl_path, "wb") as f:
        pickle.dump(huffman_codes, f)

    # return stats for display
    original_size = os.path.getsize(input_path)
    compressed_size = os.path.getsize(bin_path)
    ratio = 100 - (compressed_size / original_size * 100)

    # print stats on console
    print(f"Original: {original_size} bytes")
    print(f"Compressed: {compressed_size} bytes")
    ratio = 100 - (compressed_size / original_size * 100)
    print(f"Ratio: {ratio:.2f}%")

    return {
        "bin_path": bin_path,
        "codes_path": pkl_path,
        "original_size": original_size,
        "compressed_size": compressed_size,
        "compression_ratio": ratio,
        "huffman_codes": huffman_codes
    }