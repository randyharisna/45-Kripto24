import tkinter as tk
from tkinter import messagebox

def encrypt():
    try:
        text = entry_text.get()
        shift = int(entry_shift.get())
        encrypted_text = shift_cipher(text, shift)
        result_var.set(f"Ciphertext: {encrypted_text}")
    except ValueError:
        messagebox.showerror("Invalid shift key.","Please insert a valid number.")

def decrypt():
    try:
        text = entry_text.get()
        shift = int(entry_shift.get())
        decrypted_text = shift_cipher(text, -shift)
        result_var.set(f"Plaintext: {decrypted_text}")
    except ValueError:
        messagebox.showerror("Invalid shift key.","Please insert a valid number.")

def shift_cipher(text, shift):
    result = ""
    for char in text:
        if char.isupper():
            result += chr((ord(char) + shift - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            result += char
    return result

root = tk.Tk()
root.title("Shift Cipher (Caesar Cipher)")
root.configure(bg = "#f2f2f2")

label_text = tk.Label(root, text="Enter text:")
label_text.grid(row=0, column=0, padx=10, pady=10)

entry_text = tk.Entry(root, width=30)
entry_text.grid(row=0, column=1, padx=10, pady=10)

label_shift = tk.Label(root, text="Enter shift value:")
label_shift.grid(row=1, column=0, padx=10, pady=10)

entry_shift = tk.Entry(root, width=10)
entry_shift.grid(row=1, column=1, padx=10, pady=10)

result_var = tk.StringVar()
label_result = tk.Label(root, textvariable=result_var, font=("Segoe UI", 12))
label_result.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

button_encrypt = tk.Button(root, text="Encrypt", command=encrypt)
button_encrypt.grid(row=2, column=0, padx=10, pady=10)

button_decrypt = tk.Button(root, text="Decrypt", command=decrypt)
button_decrypt.grid(row=2, column=1, padx=10, pady=10)

root.mainloop()
