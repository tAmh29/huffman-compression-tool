# Implementation of Min-Heap & Huffman Tree

import heapq
from collections import Counter
from huffman_codes import build_codes

class HuffmanNode:
    def __init__(self, char, freq):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

# Comparison Operator for Min-Heap sorting (heapq)
    def __lt__(self, other):
        return self.freq < other.freq
    
def build_huffman_tree(freq_map):
    # Creates Min-Heap
    heap = [HuffmanNode(char, freq) for char, freq in freq_map.items()]
    heapq.heapify(heap)
    
    # Merge nodes until we have one root node

    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        new_node = HuffmanNode(None, left.freq + right.freq)
        new_node.left = left
        new_node.right = right
        heapq.heappush(heap, new_node)

    return heap[0]