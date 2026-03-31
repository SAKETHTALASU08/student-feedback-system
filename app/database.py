import sqlite3

DB_NAME = "feedback.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS feedback (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            message TEXT NOT NULL
        )
    ''')
    conn.close()

def insert_feedback(name, message):
    conn = get_connection()
    conn.execute(
        'INSERT INTO feedback (name, message) VALUES (?, ?)',
        (name, message)
    )
    conn.commit()
    conn.close()

def get_all_feedback():
    conn = get_connection()
    data = conn.execute(
        'SELECT name, message FROM feedback ORDER BY id DESC'
    ).fetchall()
    conn.close()
    return data