import hashlib
import sqlite3
import logging

logger = logging.getLogger('StudentSystem.auth')


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register(cursor, conn):
    logger.info("Начало процесса регистрации нового пользователя")

    print("-------------------------")
    print("--------Register---------")
    print("-------------------------")
    id = input("Enter your Id: ")
    password = input("Enter your Password: ")
    hashed_password = hash_password(password)

    try:
        cursor.execute("INSERT INTO admin VALUES (?, ?)", (id, hashed_password))
        conn.commit()
        logger.info(f"Успешная регистрация пользователя с ID: {id}")
        print("Registered successfully!")
    except sqlite3.IntegrityError:
        logger.warning(f"Попытка регистрации существующего пользователя: {id}")
        print("User already exists!")
    except Exception as e:
        logger.error(f"Ошибка при регистрации пользователя {id}: {e}")
        print(f"Registration error: {e}")

    input("Press Enter to continue!")

    logger.info("Автоматический вход после регистрации")
    return login(cursor)


def login(cursor):
    logger.info("Начало процесса авторизации")

    print("-------------")
    print("--- login ---")
    print("-------------")
    id = input("Enter the id: ")
    password = input("Enter the password: ")
    hashed_password = hash_password(password)

    cursor.execute(
        "SELECT * FROM admin WHERE id = ? AND password = ?", (id, hashed_password)
    )
    result = cursor.fetchall()

    if len(result) == 1:
        logger.info(f"Успешный вход пользователя: {id}")
        print("-------------------------------------")
        print(f"--Welcome {id}, what you want to do!--")
        print("-------------------------------------")
        return True
    else:
        logger.warning(f"Неудачная попытка входа для пользователя: {id}")
        print("Invalid credentials!")
        return False
