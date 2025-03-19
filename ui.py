import tkinter as tk
from tkinter import filedialog, PhotoImage
import os

def openfile():
    filename = filedialog.askopenfilename(initialdir="/", title="Select An Image", filetypes=(("Text Files", "*.txt"), ("Binary Files", "*.bin")))
    file_input.insert(0, filename)

root = tk.Tk()
root.title("Huffman Compression Tool")
root.geometry("1000x600")
# const
BODY_FONT = ("Segoe UI", 10)

# set icon
# icon_dir = os.path.dirname(os.path.abspath(__file__))
# browse_icon = PhotoImage(file=os.path.join(icon_dir, "package.png"))
# compress_icon = PhotoImage(file=os.path.join(icon_dir, "compress.png"))
# decompress_icon = PhotoImage(file=os.path.join(icon_dir, "decompress.png"))


# create file input
file_input = tk.Entry(root, width=50)
file_input.pack(pady=20)

browse_button = tk.Button(root, text="Browse", width=10, command=openfile)
browse_button.pack(pady=10)

compression_label = tk.Label(root, text="Compressed Size will be here", font=BODY_FONT, fg="blue", compound=tk.LEFT)
compression_label.pack(pady=5)

compress_button = tk.Button(root, text="Compress", command=lambda: print("Compress Clicked"), width=10)
compress_button.pack(pady=10)

tk.Label(root, text="Huffman Codes:", font=("Arial", 10, "bold")).pack(pady=5)

codes_frame = tk.Frame(root)
codes_frame.pack()

scrollbar = tk.Scrollbar(codes_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

huffman_text = tk.Text(codes_frame, height=8, width=50, yscrollcommand=scrollbar.set)
huffman_text.pack()
scrollbar.config(command=huffman_text.yview)

decompress_button = tk.Button(root, text="Decompress", compound=tk.LEFT, command=lambda: print("Decompress Clicked"))
decompress_button.pack(pady=10)

codes_frame = tk.Frame(root)
codes_frame.pack()

scrollbar = tk.Scrollbar(codes_frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

decoded_text = tk.Text(codes_frame, height=8, width=50, yscrollcommand=scrollbar.set)
decoded_text.pack()

exit_button = tk.Button(root, text="Exit", command=root.quit, width=10)
exit_button.pack(pady=10)

root.mainloop()