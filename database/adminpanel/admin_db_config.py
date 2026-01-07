import sqlite3
import hashlib
def create_connection():
    """ create a database connection to the SQLite database specified by db_file """
    conn = None
    try:
        conn = sqlite3.connect("zyntra_db.sqlite")
    except sqlite3.Error as e:
        print(e)
    return conn

def setup_database():
    conn = create_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password TEXT NOT NULL,
            role TEXT DEFAULT 'admin'
        )
    ''')
    conn.commit()
    conn.close()


def check_login_panel(conn, username, password):
    """ Check if the provided username and password match an entry in the admin panel table """
    conn = create_connection()
    cursor = conn.cursor()
    hashed_pw = hashlib.sha256(password.encode()).hexdigest()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, hashed_pw))
    user = cursor.fetchone()
    conn.close()
    return user