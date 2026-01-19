import sqlite3
import logging

logger = logging.getLogger('StudentSystem.database')


def init_database():
    logger.info("SQLite database initialized")

    try:
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        logger.info("Connection to the database has been established successfully")

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS studentsinfo(
                sch_no INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                email TEXT,
                phone TEXT
            )
        ''')
        logger.info("Table studentsinfo created")

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS admin(
                id TEXT PRIMARY KEY,
                password TEXT
            )
        ''')
        logger.info("Table admin created")

        conn.commit()
        logger.info("The database is ready for use")

        return conn, cursor

    except Exception as e:
        logger.error(f"Database initialization error: {e}", exc_info=True)
        raise
