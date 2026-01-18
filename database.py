import sqlite3
import logging

logger = logging.getLogger('StudentSystem.database')


def init_database():
    logger.info("Инициализация базы данных SQLite")

    try:
        conn = sqlite3.connect('students.db')
        cursor = conn.cursor()
        logger.info("Подключение к базе данных успешно установлено")

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS studentsinfo(
                sch_no INTEGER PRIMARY KEY,
                name TEXT,
                age INTEGER,
                email TEXT,
                phone TEXT
            )
        ''')
        logger.info("Таблица studentsinfo проверена/создана")

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS admin(
                id TEXT PRIMARY KEY,
                password TEXT
            )
        ''')
        logger.info("Таблица admin проверена/создана")

        conn.commit()
        logger.info("База данных готова к использованию")

        return conn, cursor

    except Exception as e:
        logger.error(f"Ошибка инициализации базы данных: {e}")
        raise
