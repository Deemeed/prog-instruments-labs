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
    logger.info("Пользователь завершил работу программы")
    print("---------------------------------")
    print(" Thank you for using our system!")
    print("    Created by Siddharth Jain")
    print("       Have a nice day :)")
    print("---------------------------------")


def start(conn, cursor):
    logger.info("Начало работы с системой")
    print("-------------------------------------")
    print(" Welcome to Student Management System")
    print("-------------------------------------")
    print("1: Login")
    print("2: Register")

    choice = input("Enter your choice: ")

    if choice == "1":
        logger.info("Пользователь выбрал вход в систему")
        if login(cursor):
            logger.info("Успешный вход в систему")
            return True
        else:
            logger.warning("Неудачная попытка входа")
            return start(conn, cursor)
    elif choice == "2":
        logger.info("Пользователь выбрал регистрацию")
        if register(cursor, conn):
            logger.info("Успешная регистрация и вход")
            return True
        else:
            return start(conn, cursor)
    else:
        logger.warning(f"Некорректный выбор в меню старта: {choice}")
        print("Invalid choice!")
        return start(conn, cursor)


def main():
    logger.info("Программа инициализирована")

    try:
        conn, cursor = init_database()
        logger.info("База данных успешно инициализирована")
    except Exception as e:
        logger.error(f"Ошибка инициализации базы данных: {e}")
        print(f"Database error: {e}")
        return

    if not start(conn, cursor):
        return

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        logger.info(f"Пользователь выбрал опцию: {choice}")

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
            logger.warning(f"Неверный выбор в главном меню: {choice}")
            print("Invalid choice!")


if __name__ == "__main__":
    main()
