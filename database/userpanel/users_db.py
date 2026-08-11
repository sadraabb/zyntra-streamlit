# imports
import sqlite3
import hashlib
import os

# مسیر پوشه و فایل دیتابیس (مستقل از اینکه برنامه از کجا اجرا می‌شود)
DB_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), ".user_data_folder")
DB_PATH = os.path.join(DB_DIR, "users.db")

def get_connection():
    # اگر پوشه‌ی دیتابیس وجود نداشته باشد (مثلاً روی دیپلوی تازه)، بسازش
    os.makedirs(DB_DIR, exist_ok=True)
    return sqlite3.connect(DB_PATH)

def create_users_table():
    conn = get_connection()
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
    _seed_demo_user(conn)
    conn.close() # بستن اتصال برای امنیت و مدیریت حافظه

def _seed_demo_user(conn):
    """
    یوزر دمو (demo/demo123) رو اگر وجود نداشته باشه می‌سازه.
    اینجوری روی هر دیپلوی تازه (که دیتابیس خالیه) هم بنر دمو توی main.py معتبر می‌مونه.
    idempotent هست: اگر از قبل وجود داشته باشه، هیچ کاری نمی‌کنه.
    """
    cursor = conn.cursor()
    cursor.execute('SELECT 1 FROM users WHERE user_name = ?', ('demo',))
    if cursor.fetchone() is None:
        demo_password_hash = hashlib.sha256('demo123'.encode()).hexdigest()
        cursor.execute('''
            INSERT INTO users (user_name, name, last_name, password_hash, email)
            VALUES (?, ?, ?, ?, ?)
        ''', ('demo', 'کاربر', 'دمو', demo_password_hash, 'demo@zyntra.local'))
        conn.commit()

def add_user(user_name, name, last_name, password, email):
    try:
        password_hash = hashlib.sha256(password.encode()).hexdigest()
        conn = get_connection()
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

# دریافت اطلاعات کاربر بر اساس نام کاربری
def get_user_by_username(user_name):
    with get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM users WHERE user_name = ?', (user_name,))
        user = cursor.fetchone()
        return user
# وریفای رمز عبور
def verify_password(password, password_hash):
    return hashlib.sha256(password.encode()).hexdigest() == password_hash
# بررسی اعتبار ورود
def check_vaild_login(user_name, password):
    user = get_user_by_username(user_name)
    if user:
        stored_password_hash = user[4]  # ایندکس 4 مربوط به password_hash است
        if verify_password(password, stored_password_hash):
            return True, user  # بازگرداندن True و اطلاعات کاربر در صورت موفقیت
    return False, None  # بازگرداندن False در صورت عدم موفقیت