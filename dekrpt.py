import tkinter as tk
from tkinter import filedialog

def decrypt_text(input_file, output_file, key):
    try:
        with open(input_file, 'r') as f:
            encrypted_text = f.read().lower()
    except FileNotFoundError:
        return "Input file not found."

    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    key_length = len(key)
    decrypted_text = ""
    for i, letter in enumerate(encrypted_text):
        if letter in alphabet:
            shift = alphabet.find(key[i % key_length])
            decrypted_text += alphabet[(alphabet.index(letter) - shift) % 26]
        else:
            decrypted_text += letter

    try:
        with open(output_file, 'w') as f:
            f.write(decrypted_text)
        return "Decrypted text saved to " + output_file
    except Exception as e:
        return "Error writing to output file: " + str(e)

def browse_file(entry):
    path = filedialog.askopenfilename()
    entry.delete(0, tk.END)
    entry.insert(0, path)

def decrypt():
    input_file = input_entry.get()
    output_file = output_entry.get()
    key = key_entry.get()
    result = decrypt_text(input_file, output_file, key)
    result_label.config(text=result)

window = tk.Tk()
window.title("Text File Decryption")
window.resizable(False, False)

input_label = tk.Label(window, text="Input File:")
input_label.grid(row=0, column=0, padx=5, pady=5)
input_entry = tk.Entry(window, width=30)
input_entry.grid(row=0, column=1, padx=5, pady=5)
input_button = tk.Button(window, text="Browse", command=lambda: browse_file(input_entry))
input_button.grid(row=0, column=2, padx=5, pady=5)

output_label = tk.Label(window, text="Output File:")
output_label.grid(row=1, column=0, padx=5, pady=5)
output_entry = tk.Entry(window, width=30)
output_entry.grid(row=1, column=1, padx=5, pady=5)

key_label = tk.Label(window, text="Key:")
key_label.grid(row=2, column=0, padx=5, pady=5)
key_entry = tk.Entry(window, width=30)
key_entry.grid(row=2, column=1, padx=5, pady=5)

decrypt_button = tk.Button(window, text="Decrypt", command=decrypt)
decrypt_button.grid(row=3, column=1, padx=5, pady=5)

result_label = tk.Label(window, text="", fg="green")
result_label.grid(row=4, column=1, padx=5, pady=5)

window.mainloop()
