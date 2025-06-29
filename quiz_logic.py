from db import connect_db

class QuizManager:
    def __init__(self):
        self.conn = connect_db()
        self.cursor = self.conn.cursor()
        self.questions = self.load_questions()
        self.index = 0
        self.score = 0
        self.username = ""

    def load_questions(self):
        self.cursor.execute("SELECT * FROM Questions")
        return self.cursor.fetchall()

    def get_next_question(self):
        if self.index < len(self.questions):
            q = self.questions[self.index]
            self.index += 1
            return {
                'id': q.QuestionID,
                'text': q.QuestionText,
                'options': [q.OptionA, q.OptionB, q.OptionC, q.OptionD],
                'answer': q.CorrectOption
            }
        else:
            return None

    def check_answer(self, selected_option, correct_option):
        if selected_option == correct_option:
            self.score += 1
