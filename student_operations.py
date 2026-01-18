import sqlite3
import logging

logger = logging.getLogger('StudentSystem.operations')


def add_student(cursor, conn):
    logger.info("Начало добавления нового студента")

    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    var1 = input("Enter the sch no. of the student: ")
    var2 = input("Enter the name of the student: ")
    var3 = input("Enter the age of the student: ")
    var4 = input("Enter the email of the student: ")
    var5 = input("Enter the phone no. of the student: ")

    try:
        cursor.execute(
            "INSERT INTO studentsinfo VALUES (?, ?, ?, ?, ?)",
            (var1, var2, var3, var4, var5)
        )
        conn.commit()
        logger.info(f"Студент добавлен: {var2} (sch_no: {var1})")
        print("Data saved successfully!")
    except sqlite3.IntegrityError:
        logger.warning(f"Попытка добавления студента с существующим sch_no: {var1}")
        print("Student with this sch_no already exists!")
    except Exception as e:
        logger.error(f"Ошибка при добавлении студента {var1}: {e}")
        print(f"Error saving data: {e}")

    input("Press Enter to continue!")


def view_students(cursor):
    logger.info("Просмотр списка всех студентов")

    print("------------------------")
    print("--- Student Records ---")
    print("------------------------")

    try:
        cursor.execute("SELECT * FROM studentsinfo")
        students = cursor.fetchall()

        if len(students) == 0:
            logger.info("В базе данных нет записей о студентах")
            print("No students found in database")
        else:
            logger.info(f"Найдено {len(students)} студентов")
            for i in students:
                print(i)
    except Exception as e:
        logger.error(f"Ошибка при получении списка студентов: {e}")
        print(f"Error viewing students: {e}")

    input("Press Enter to continue!")


def search_student(cursor):
    logger.info("Поиск студента по номеру")

    print("------------------------")
    print("--- Search Student ---")
    print("------------------------")
    a = input("Enter the sch no. of the student: ")

    logger.info(f"Поиск студента с sch_no: {a}")

    try:
        cursor.execute("SELECT * FROM studentsinfo WHERE sch_no = ?", (a,))
        result = cursor.fetchall()

        if len(result) == 0:
            logger.warning(f"Студент с sch_no {a} не найден")
            print("Enter valid sch no.!")
        else:
            logger.info(f"Найден студент с sch_no {a}")
            for i in result:
                print(i)
    except Exception as e:
        logger.error(f"Ошибка при поиске студента {a}: {e}")
        print(f"Error searching student: {e}")

    input("Press Enter to continue!")


def update_student(cursor, conn):
    logger.info("Обновление данных студента")

    print("------------------------")
    print("--- Update Student ---")
    print("------------------------")
    sch_no = input("Enter the sch no. of the student: ")
    name = input("Enter the name of the student: ")
    age = input("Enter the age of the student: ")
    email = input("Enter the email of the student: ")
    phone = input("Enter the phone no. of the student: ")

    logger.info(f"Обновление данных студента с sch_no: {sch_no}")

    try:
        cursor.execute(
            "UPDATE studentsinfo SET name = ?, age = ?, email = ?, phone = ? WHERE sch_no = ?",
            (name, age, email, phone, sch_no)
        )

        if cursor.rowcount == 0:
            logger.warning(f"Студент с sch_no {sch_no} не найден для обновления")
            print("Student not found!")
        else:
            conn.commit()
            logger.info(f"Данные студента {sch_no} успешно обновлены")
            print("Data updated successfully!")
    except Exception as e:
        logger.error(f"Ошибка при обновлении студента {sch_no}: {e}")
        print(f"Error updating data: {e}")

    input("Press Enter to continue!")


def delete_student(cursor, conn):
    logger.info("Удаление студента")

    print("------------------------")
    print("--- Delete Student ---")
    print("------------------------")
    var1 = input("Enter the sch no. of the student: ")

    logger.info(f"Удаление студента с sch_no: {var1}")

    try:
        cursor.execute("DELETE FROM studentsinfo WHERE sch_no = ?", (var1,))

        if cursor.rowcount == 0:
            logger.warning(f"Студент с sch_no {var1} не найден для удаления")
            print("Student not found!")
        else:
            conn.commit()
            logger.info(f"Студент с sch_no {var1} успешно удален")
            print("Data deleted successfully!")
    except Exception as e:
        logger.error(f"Ошибка при удалении студента {var1}: {e}")
        print(f"Error deleting data: {e}")

    input("Press Enter to continue!")
