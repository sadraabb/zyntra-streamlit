# imports
import sqlite3
import hashlib

def create_users_table():
    conn = sqlite3.connect('./database/userpanel/.user_data_folder/users.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_name TEXT NOT NULL UNIQUE,
            name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            password_hash TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    ''')
    conn.commit()
    conn.close() # بستن اتصال برای امنیت و مدیریت حافظه

def add_user(user_name, name, last_name, password, email):
    try:
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        conn = sqlite3.connect('./database/userpanel/.user_data_folder/users.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO users (user_name, name, last_name, password_hash, email)
            VALUES (?, ?, ?, ?, ?)
        ''', (user_name, name, last_name, password_hash, email))
        
        new_user_id = cursor.lastrowid
        conn.commit()
        conn.close()
        return new_user_id, "SUCCESS"

    except sqlite3.IntegrityError:
        # این خطا زمانی رخ می‌دهد که UNIQUE بودن یوزرنیم یا ایمیل نقض شود
        return None, "DUPLICATE"
    except Exception as e:
        # برای خطاهای پیش‌بینی نشده دیگر
        return None, str(e)