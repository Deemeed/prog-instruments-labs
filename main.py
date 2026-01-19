from auth import register, login
from database import init_database
from student_operations import add_student, view_students, search_student, update_student, delete_student
from logger import setup_logging

logger = setup_logging()


def display_menu():
    print("\n1: Add New Student")
    print("2: View Students")
    print("3: Search Student")
    print("4: Update Student")
    print("5: Delete Student")
    print("6: Exit")


def exit_program():
    logger.info("The user has completed the program")
    print("---------------------------------")
    print(" Thank you for using our system!")
    print("    Created by Siddharth Jain")
    print("       Have a nice day :)")
    print("---------------------------------")


def start(conn, cursor):
    logger.info("System started")
    print("-------------------------------------")
    print(" Welcome to Student Management System")
    print("-------------------------------------")
    print("1: Login")
    print("2: Register")

    choice = input("Enter your choice: ")

    if choice == "1":
        logger.info("User chose to login")
        if login(cursor):
            logger.info("Login successfully")
            return True
        else:
            logger.warning("Login unsuccessfully")
            return start(conn, cursor)
    elif choice == "2":
        logger.info("User chose to register")
        if register(cursor, conn):
            logger.info("Register and login successfully")
            return True
        else:
            return start(conn, cursor)
    else:
        logger.warning(f"Invalid choice in start menu: {choice}")
        print("Invalid choice!")
        return start(conn, cursor)


def main():
    logger.info("Program initialized")

    try:
        conn, cursor = init_database()
        logger.info("Database initialized successfully")
    except Exception as e:
        logger.error(f"Database initialization error: {e}", exc_info=True)
        print(f"Database error: {e}")
        return

    if not start(conn, cursor):
        return

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        logger.info(f"User choice: {choice}")

        if choice == "1":
            add_student(cursor, conn)
        elif choice == "2":
            view_students(cursor)
        elif choice == "3":
            search_student(cursor)
        elif choice == "4":
            update_student(cursor, conn)
        elif choice == "5":
            delete_student(cursor, conn)
        elif choice == "6":
            exit_program()
            break
        else:
            logger.warning(f"Invalid choice: {choice}")
            print("Invalid choice!")


if __name__ == "__main__":
    main()
