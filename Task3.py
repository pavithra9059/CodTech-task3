import tkinter as tk
import random
import string

# ---------------- Function: Generate Password ----------------
def generate_password():
    try:
        length = int(entry.get())

        if length <= 0:
            result_var.set("Enter valid length")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))

        result_var.set(password)

    except:
        result_var.set("Invalid Input")


# ---------------- Function: Copy Password ----------------
def copy_password():
    root.clipboard_clear()
    root.clipboard_append(result_var.get())


# ---------------- Main Window ----------------
root = tk.Tk()
root.title("Password Generator")
root.geometry("420x320")
root.configure(bg="#87CEEB")   # ☁️ SKY BLUE BACKGROUND

# ---------------- Title ----------------
title = tk.Label(
    root,
    text="🔐 Password Generator",
    font=("Arial", 18, "bold"),
    bg="#87CEEB",
    fg="#0B2F4F"
)
title.pack(pady=15)

# ---------------- Input Label ----------------
label = tk.Label(
    root,
    text="Enter Password Length:",
    font=("Arial", 12, "bold"),
    bg="#87CEEB",
    fg="#0B2F4F"
)
label.pack()

# ---------------- Entry Box ----------------
entry = tk.Entry(
    root,
    font=("Arial", 14),
    justify="center",
    bg="#FFFFFF",
    fg="black",
    width=10
)
entry.pack(pady=8)

# ---------------- Generate Button ----------------
btn_generate = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 12, "bold"),
    bg="#1E90FF",
    fg="white",
    activebackground="#00BFFF",
    activeforeground="white",
    command=generate_password,
    padx=10,
    pady=5
)
btn_generate.pack(pady=8)

# ---------------- Result Box ----------------
result_var = tk.StringVar()

result_box = tk.Label(
    root,
    textvariable=result_var,
    font=("Arial", 14, "bold"),
    bg="#E0F7FF",
    fg="#FF4500",
    width=30,
    height=2
)
result_box.pack(pady=12)

# ---------------- Copy Button ----------------
btn_copy = tk.Button(
    root,
    text="Copy Password 📋",
    font=("Arial", 11, "bold"),
    bg="#4682B4",
    fg="white",
    activebackground="#5DADE2",
    command=copy_password
)
btn_copy.pack(pady=5)

root.mainloop()
