# File containing Generating Huffman Codes Function
import heapq

def build_codes(node, prefix="", code_map={}):
    if node is None:
        return
    
    if node.char is not None:
        code_map[node.char] = prefix

    build_codes(node.left, prefix + "0", code_map) # left child (0)
    build_codes(node.right, prefix + "1", code_map) # right child (1)

    return code_map
