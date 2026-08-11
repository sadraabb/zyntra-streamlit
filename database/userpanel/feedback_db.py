# feedback_db.py
import sqlite3
import os

# مسیر مستقل از محل اجرای برنامه، داخل همون پوشه‌ی مخفی کاربران
DB_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".user_data_folder")
DB_FILE = os.path.join(DB_DIR, "feedback.db")

def get_connection():
    os.makedirs(DB_DIR, exist_ok=True)
    return sqlite3.connect(DB_FILE)

def init_feedback_db():
    conn = get_connection()
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
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO feedback (name, feedback_text, issue_type, rating)
        VALUES (?, ?, ?, ?)
    """, (name, feedback_text, issue_type, rating))
    conn.commit()
    conn.close()
