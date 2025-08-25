import tkinter as tk
from tkinter import messagebox
import math

def encrypt_message(key, message):
    ciphertext = [''] * key
    for column in range(key):
        pointer = column
        while pointer < len(message):
            ciphertext[column] += message[pointer]
            pointer += key
    return ''.join(ciphertext)

def decrypt_message(key, message):
    num_columns = math.ceil(len(message) / key)
    num_rows = key
    num_shaded_boxes = (num_columns * num_rows) - len(message)
    plaintext = [''] * num_columns

    col = 0
    row = 0
    for symbol in message:
        plaintext[col] += symbol
        col += 1
        if (col == num_columns) or (col == num_columns -1 and row >= num_rows - num_shaded_boxes):
            col = 0
            row += 1

    return ''.join(plaintext)

def encrypt():
    try:
        key = int(key_entry.get())
        message = message_text.get("1.0", tk.END).rstrip('\n')
        if key <= 0:
            messagebox.showerror("Error", "Key must be a positive integer.")
            return
        encrypted = encrypt_message(key, message)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, encrypted)
    except ValueError:
        messagebox.showerror("Error", "Invalid key. Please enter a positive integer.")

def decrypt():
    try:
        key = int(key_entry.get())
        message = message_text.get("1.0", tk.END).rstrip('\n')
        if key <= 0:
            messagebox.showerror("Error", "Key must be a positive integer.")
            return
        decrypted = decrypt_message(key, message)
        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, decrypted)
    except ValueError:
        messagebox.showerror("Error", "Invalid key. Please enter a positive integer.")

# GUI Setup
root = tk.Tk()
root.title("Columnar Transposition Cipher")

tk.Label(root, text="Enter Key (positive integer):").grid(row=0, column=0, padx=10, pady=5, sticky='w')
key_entry = tk.Entry(root)
key_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Enter Message:").grid(row=1, column=0, padx=10, pady=5, sticky='nw')
message_text = tk.Text(root, height=5, width=50)
message_text.grid(row=1, column=1, padx=10, pady=5)

encrypt_button = tk.Button(root, text="Encrypt", command=encrypt)
encrypt_button.grid(row=2, column=0, padx=10, pady=10)

decrypt_button = tk.Button(root, text="Decrypt", command=decrypt)
decrypt_button.grid(row=2, column=1, padx=10, pady=10, sticky='w')

tk.Label(root, text="Output:").grid(row=3, column=0, padx=10, pady=5, sticky='nw')
output_text = tk.Text(root, height=5, width=50)
output_text.grid(row=3, column=1, padx=10, pady=5)

root.mainloop()
