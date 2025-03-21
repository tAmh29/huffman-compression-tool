# File that reads .txt file & counts character frequencies
from collections import Counter

def count_char_freq(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    frequency = Counter(text)

    return frequency