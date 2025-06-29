import tkinter as tk
from tkinter import messagebox
from db import add_user

def open_register():
    BG_COLOR = "#dceeff"
    reg = tk.Toplevel()
    reg.title("Register")
    reg.geometry("400x300")
    reg.configure(bg=BG_COLOR)

    tk.Label(reg, text="Register", font=("Arial", 18, "bold"), bg=BG_COLOR).pack(pady=10)

    tk.Label(reg, text="Username:", bg=BG_COLOR).pack()
    username_entry = tk.Entry(reg)
    username_entry.pack()

    tk.Label(reg, text="Password:", bg=BG_COLOR).pack()
    password_entry = tk.Entry(reg, show="*")
    password_entry.pack()

    def register_user():
        if add_user(username_entry.get(), password_entry.get()):
            messagebox.showinfo("Success", "Registered successfully!")
            reg.destroy()
        else:
            messagebox.showerror("Error", "Username already exists")

    tk.Button(reg, text="Register", command=register_user, bg="blue", fg="white").pack(pady=15)
    tk.Button(reg, text="Back", command=reg.destroy, bg="gray", fg="white").pack()
