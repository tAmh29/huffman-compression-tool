import tkinter as tk
from tkinter import filedialog, messagebox
import os
import pickle
from huffman_compress import compress_file_to_disk

# ---------- Functions ----------
# Function to open file dialog and select a file
def openfile():
    filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetypes=(("Text Files", "*.txt"), ("Compressed Files", "*.bin")))
    if filename:
        file_input.delete(0, tk.END)
        file_input.insert(0, filename)

# Function to compress the selected file
def compress_file():
    file_path = file_input.get()
    
    if not file_path:
        messagebox.showerror("Error", "Please select a file first")
        return

    try:
        result = compress_file_to_disk(file_path)

        # Display Huffman codes
        huffman_text.delete(1.0, tk.END)
        for char, code in sorted(result["huffman_codes"].items()):
            label = repr(char).replace(" ", "'SPACE'").replace("\\n", "'NEWLINE'")
            huffman_text.insert(tk.END, f"{label}: {code}\n")

        # Update stats
        compression_label.config(
            text=f"Original: {result['original_size']} bytes, "
                 f"Compressed: {result['compressed_size']} bytes, "
                 f"Ratio: {result['compression_ratio']:.2f}%"
        )

        messagebox.showinfo("Success", f"File compressed successfully!\nSaved to: {result['bin_path']}")

    except Exception as e:
        messagebox.showerror("Error", f"Compression failed: {str(e)}")


# Function to decompress the selected file
def decompress_file():
    input_path = file_input.get()
    
    if not input_path:
        messagebox.showerror("Error", "Please select a file.")
        return

    # find compressed file and codes file
    compressed_path = os.path.splitext(input_path)[0] + "_compressed.bin"
    codes_path = os.path.splitext(input_path)[0] + "_codes.pkl"

    if not os.path.exists(compressed_path):
        messagebox.showerror("Error", f"Compressed file not found: {compressed_path}")
        return

    if not os.path.exists(codes_path):
        messagebox.showerror("Error", f"Codes file not found: {codes_path}")
        return

    # Load Huffman Codes from file
    try:
        with open(codes_path, "rb") as f:
            huffman_codes = pickle.load(f)
    except FileNotFoundError:
        messagebox.showerror("Error", "Huffman codes file not found.")
        return

    reverse_codes = {v: k for k, v in huffman_codes.items()}

    # Read compressed binary file
    with open(compressed_path, "rb") as f:
        binary_data = f.read()

    # Convert bytes to binary string
    binary_string = "".join(f"{byte:08b}" for byte in binary_data)

    # Remove padding
    padding_length = int(binary_string[:8], 2)
    binary_string = binary_string[8:-padding_length] if padding_length > 0 else binary_string

    # Decode text using Huffman codes
    decoded_text = ""
    temp_code = ""
    for bit in binary_string:
        temp_code += bit
        if temp_code in reverse_codes:
            decoded_text += reverse_codes[temp_code]
            temp_code = ""

    # Display decoded text in UI
    decoded_text_area.delete(1.0, tk.END)
    decoded_text_area.insert(tk.END, decoded_text)

    messagebox.showinfo("Success", "File decompressed successfully!")

# ---------- main menu ----------

root = tk.Tk()
root.title("Huffman Compression Tool")
root.geometry("1000x600")
# const
BODY_FONT = ("Segoe UI", 10)

# create file input
file_input = tk.Entry(root, width=50)
file_input.pack(pady=20)

# create browse button
browse_button = tk.Button(root, text="Browse", width=10, command=openfile)
browse_button.pack(pady=10)

# create compression label and compress button
compression_label = tk.Label(root, text="Compressed Size will be here", font=BODY_FONT, fg="blue", compound=tk.LEFT)
compression_label.pack(pady=5)

compress_button = tk.Button(root, text="Compress", command=compress_file, width=10)
compress_button.pack(pady=10)

# create huffman codes label and text area
tk.Label(root, text="Huffman Codes:", font=("Arial", 10, "bold")).pack(pady=5)

codes_frame = tk.Frame(root)
codes_frame.pack()

scrollbar = tk.Scrollbar(codes_frame) # create scrollbar
scrollbar.pack(side=tk.RIGHT, fill=tk.Y) # pack scrollbar to the right side of the frame

# create text area for huffman codes
huffman_text = tk.Text(codes_frame, height=8, width=60, yscrollcommand=scrollbar.set)
huffman_text.pack()
scrollbar.config(command=huffman_text.yview)

# create decompression label and decompress button
decompress_button = tk.Button(root, text="Decompress", command=decompress_file, width=10)
decompress_button.pack(pady=10)

codes_frame = tk.Frame(root)
codes_frame.pack()

scrollbar = tk.Scrollbar(codes_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# create text area for decoded text
decoded_text_area = tk.Text(codes_frame, height=8, width=60, yscrollcommand=scrollbar.set)
decoded_text_area.pack()
scrollbar.config(command=decoded_text_area.yview)


exit_button = tk.Button(root, text="Exit", command=root.quit, width=10)
exit_button.pack(pady=10)

root.mainloop()