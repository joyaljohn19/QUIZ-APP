import tkinter as tk
from db import get_top_scores

def open_leaderboard():
    lb = tk.Tk()
    lb.title("Leaderboard")
    lb.geometry("500x400")
    lb.configure(bg="#dceeff")

    tk.Label(lb, text="🏆 Leaderboard", font=("Arial", 18, "bold"), bg="#dceeff").pack(pady=10)

    headers = ["Username", "Score", "Date"]
    for i, h in enumerate(headers):
        tk.Label(lb, text=h, font=("Arial", 12, "bold"), bg="#dceeff", fg="black", width=15).grid(row=1, column=i, padx=5)

    scores = get_top_scores()
    for i, row in enumerate(scores, start=2):
        for j, val in enumerate(row):
            tk.Label(lb, text=str(val), font=("Arial", 12), bg="#dceeff").grid(row=i, column=j, padx=5)

    tk.Button(lb, text="Close", command=lb.destroy,
              bg="gray", fg="white", font=("Arial", 12)).pack(pady=20)