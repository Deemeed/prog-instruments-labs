import sqlite3


def init_database():
    conn = sqlite3.connect('students.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS studentsinfo(
            sch_no INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            email TEXT,
            phone TEXT
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS admin(
            id TEXT PRIMARY KEY,
            password TEXT
        )
    ''')

    conn.commit()
    return conn, cursor
