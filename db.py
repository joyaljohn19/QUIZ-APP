import pyodbc

def connect_db():
    return pyodbc.connect(
        'DRIVER={SQL Server};'
        'SERVER=DESKTOP-USJNA54;'  # Update if your SQL Server name is different
        'DATABASE=QuizGameDB;'
        'Trusted_Connection=yes;'
    )

def add_user(username, password):
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Users (Username, Password) VALUES (?, ?)", (username, password))
        conn.commit()
        return True
    except:
        return False

def get_user(username, password):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Users WHERE Username = ? AND Password = ?", (username, password))
    return cursor.fetchone()

def save_score(username, score):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Scores (Username, Score) VALUES (?, ?)", (username, score))
    conn.commit()

def get_top_scores(limit=10):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT Username, Score, AttemptedOn FROM Scores ORDER BY Score DESC, AttemptedOn ASC")
    return cursor.fetchall()
