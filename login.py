import tkinter as tk
from tkinter import messagebox
from db import get_user
from register import open_register
from main import start_quiz

def open_login():
    root = tk.Tk()
    root.title("Login")
    root.geometry("400x300")
    BG_COLOR = "#dceeff"
    root.configure(bg=BG_COLOR)

    tk.Label(root, text="Login", font=("Arial", 18, "bold"), bg=BG_COLOR).pack(pady=10)

    tk.Label(root, text="Username:", bg=BG_COLOR).pack()
    username_entry = tk.Entry(root)
    username_entry.pack()

    tk.Label(root, text="Password:", bg=BG_COLOR).pack()
    password_entry = tk.Entry(root, show="*")
    password_entry.pack()

    def login_action():
        username = username_entry.get()
        password = password_entry.get()
        user = get_user(username, password)

        if user:
            root.destroy()
            start_quiz(username)
        else:
            messagebox.showerror("Login Failed", "Invalid credentials")

    tk.Button(root, text="Login", command=login_action,
              bg="blue", fg="white", font=("Arial", 12)).pack(pady=10)

    tk.Button(root, text="Register new account", command=open_register,
              fg="blue", bg=BG_COLOR, relief="flat", font=("Arial", 12)).pack()

    root.mainloop()

# Make sure this runs when you double click the file
if __name__ == "__main__":
    open_login()

