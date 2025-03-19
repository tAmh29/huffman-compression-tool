# File that reads .txt file & counts character frequencies
from collections import Counter

def count_char_freq(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        text = f.read()

    frequency = Counter(text)

    return frequency

file_path = "input.txt"

char_frequencies = count_char_freq(file_path)

print("Character Frequencies:")

for char, freq in char_frequencies.items():
    if char == " ":
        print(f"'SPACE': {freq}")

    elif char == "\n":
        print(f"'NEWLINE': {freq}")

    else:
        print(f"'{char}': {freq}")