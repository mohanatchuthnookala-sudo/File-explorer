# File-expl
import tkinter as tk
from tkinter import filedialog

def browse_file():
    # Open file dialog to select a file
    file_path = filedialog.askopenfilename(
        title="Select a File",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    
    # Display the selected file path in the label
    if file_path:
        label_file.config(text=f"Selected File: {file_path}")
    else:
        label_file.config(text="No file selected")

# Create main window
root = tk.Tk()
root.title("File Explorer Example")
root.geometry("400x200")

# Label to show file path
label_file = tk.Label(root, text="No file selected", wraplength=350)
label_file.pack(pady=20)

# Button to open file explorer
btn_browse = tk.Button(root, text="Browse File", command=browse_file)
btn_browse.pack(pady=10)

# Run the Tkinter event loop
root.mainloop()orer
