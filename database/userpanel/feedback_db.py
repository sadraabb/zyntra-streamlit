# feedback_db.py
import sqlite3

DB_FILE = "feedback.db"

def init_feedback_db():
    conn = sqlite3.connect("feedback.db")
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            feedback_text TEXT,
            issue_type TEXT,
            rating TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_feedback(name, feedback_text, issue_type, rating):
    """ذخیره بازخورد در دیتابیس"""
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO feedback (name, feedback, issue_type, rating)
        VALUES (?, ?, ?, ?)
    """, (name, feedback_text, issue_type, rating))
    conn.commit()
    conn.close()
