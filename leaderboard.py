import tkinter as tk
from tkinter import ttk
import pyodbc

# Update with your SQL Server connection details
conn = pyodbc.connect(
    'Driver={SQL Server};'
    'Server=DESKTOP-USJNA54;'
    'Database=QuizGameDB;'
    'Trusted_Connection=yes;'
)

def show_leaderboard():
    leaderboard_window = tk.Tk()
    leaderboard_window.title("Leaderboard")
    leaderboard_window.geometry("500x400")

    title = tk.Label(leaderboard_window, text="Quiz Leaderboard", font=("Arial", 16))
    title.pack(pady=10)

    columns = ("Username", "Score")
    tree = ttk.Treeview(leaderboard_window, columns=columns, show='headings')
    tree.heading("Username", text="Username")
    tree.heading("Score", text="Score")

    tree.pack(pady=10, fill="both", expand=True)

    try:
        cursor = conn.cursor()
        cursor.execute("SELECT Username, Score FROM Scores ORDER BY Score DESC")
        rows = cursor.fetchall()

        if rows:
            for row in rows:
                tree.insert("", tk.END, values=(row.Username, row.Score))
        else:
            tree.insert("", tk.END, values=("No Data Found", "-"))

    except Exception as e:
        print("Error fetching leaderboard:", e)
        tree.insert("", tk.END, values=("Error fetching data", "-"))

    close_btn = tk.Button(leaderboard_window, text="Close", command=leaderboard_window.destroy)
    close_btn.pack(pady=10)

    leaderboard_window.mainloop()

if __name__ == "__main__":
    show_leaderboard()
