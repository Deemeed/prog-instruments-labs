import hashlib
import sqlite3


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def register(cursor, conn):
    print("-------------------------")
    print("--------Register---------")
    print("-------------------------")
    id = input("Enter your Id: ")
    password = input("Enter your Password: ")
    hashed_password = hash_password(password)

    try:
        cursor.execute("INSERT INTO admin VALUES (?, ?)", (id, hashed_password))
        conn.commit()
        print("Registered successfully!")
    except sqlite3.IntegrityError:
        print("User already exists!")

    input("Press Enter to continue!")
    return login(cursor)


def login(cursor):
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
        print("-------------------------------------")
        print(f"--Welcome {id}, what you want to do!--")
        print("-------------------------------------")
        return True
    else:
        print("Invalid credentials!")
        return False
