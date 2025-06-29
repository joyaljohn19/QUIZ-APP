import tkinter as tk
from tkinter import messagebox
from quiz_logic import QuizManager
from db import save_score
from leaderboard import open_leaderboard

def start_quiz(username):
    root = tk.Tk()
    root.title("Quiz Game")
    root.geometry("600x400")
    BG_COLOR = "#dceeff"
    root.configure(bg=BG_COLOR)

    quiz = QuizManager()
    quiz.username = username
    selected = tk.StringVar()
    options = []

    q_label = tk.Label(root, text="", wraplength=550, font=("Arial", 16, "bold"), bg=BG_COLOR)
    q_label.pack(pady=20)

    def load_question():
        q = quiz.get_next_question()
        if q:
            q_label.config(text=f"Q{quiz.index}. {q['text']}")
            for i, opt in enumerate(q['options']):
                options[i].config(text=f"{chr(65+i)}. {opt}")
            selected.set(None)
            root.current_question = q
        else:
            save_score(quiz.username, quiz.score)
            messagebox.showinfo("Quiz Complete", f"Score: {quiz.score}/{len(quiz.questions)}")
            root.destroy()
            open_leaderboard()

    def next_question():
        if not selected.get():
            messagebox.showwarning("Select Option", "Please choose an answer.")
            return
        quiz.check_answer(selected.get(), root.current_question['answer'])
        load_question()

    def logout():
        root.destroy()
        import login
        login.open_login()

    for val in ['A', 'B', 'C', 'D']:
        rb = tk.Radiobutton(root, text="", variable=selected, value=val,
                            font=("Arial", 12), bg=BG_COLOR)
        rb.pack(anchor='w', padx=40)
        options.append(rb)

    tk.Button(root, text="Next", command=next_question,
              font=("Arial", 12), bg="blue", fg="white").pack(pady=10)

    tk.Button(root, text="Logout", command=logout,
              bg="orange", fg="white", font=("Arial", 12)).pack(pady=5)

    tk.Button(root, text="Exit Quiz", command=root.destroy,
              bg="gray", fg="white", font=("Arial", 12)).pack()

    load_question()
    root.mainloop()
