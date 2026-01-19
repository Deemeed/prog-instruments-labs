import hashlib
import sqlite3
import logging

logger = logging.getLogger('StudentSystem.auth')


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register(cursor, conn):
    logger.info("Starting the new user registration process")

    print("-------------------------")
    print("--------Register---------")
    print("-------------------------")
    id = input("Enter your Id: ")
    password = input("Enter your Password: ")
    hashed_password = hash_password(password)

    try:
        cursor.execute("INSERT INTO admin VALUES (?, ?)", (id, hashed_password))
        conn.commit()
        logger.info(f"Successful registration of user with ID: {id}")
        print("Registered successfully!")
    except sqlite3.IntegrityError:
        logger.warning(f"Attempt to register an existing user: {id}", exc_info=True)
        print("User already exists!")
    except Exception as e:
        logger.error(f"Error while registering user {id}: {e}", exc_info=True)
        print(f"Registration error: {e}")

    input("Press Enter to continue!")

    logger.info("Automatic login after registration")
    return login(cursor)


def login(cursor):
    logger.info("Beginning of the authorization process")

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
        logger.info(f"Successful user login: {id}")
        print("-------------------------------------")
        print(f"--Welcome {id}, what you want to do!--")
        print("-------------------------------------")
        return True
    else:
        logger.warning(f"Failed login attempt for user: {id}")
        print("Invalid credentials!")
        return False
