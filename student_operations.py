import sqlite3
import logging

logger = logging.getLogger('StudentSystem.operations')


def add_student(cursor, conn):
    logger.info("Start adding a new student")

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
        logger.info(f"Student added: {var2} (sch_no: {var1})")
        print("Data saved successfully!")
    except sqlite3.IntegrityError:
        logger.warning(f"Attempting to add a student with an existing sch_no: {var1}", exc_info=True)
        print("Student with this sch_no already exists!")
    except Exception as e:
        logger.error(f"Error adding student {var1}: {e}", exc_info=True)
        print(f"Error saving data: {e}")

    input("Press Enter to continue!")


def view_students(cursor):
    logger.info("View a list of all students")

    print("------------------------")
    print("--- Student Records ---")
    print("------------------------")

    try:
        cursor.execute("SELECT * FROM studentsinfo")
        students = cursor.fetchall()

        if len(students) == 0:
            logger.info("There are no records of students in the database.")
            print("No students found in database")
        else:
            logger.info(f"{len(students)} students found")
            for i in students:
                print(i)
    except Exception as e:
        logger.error(f"Error while getting list of students: {e}", exc_info=True)
        print(f"Error viewing students: {e}")

    input("Press Enter to continue!")


def search_student(cursor):
    logger.info("Search for a student by number")

    print("------------------------")
    print("--- Search Student ---")
    print("------------------------")
    a = input("Enter the sch no. of the student: ")

    logger.info(f"Search for a student with sch_no: {a}")

    try:
        cursor.execute("SELECT * FROM studentsinfo WHERE sch_no = ?", (a,))
        result = cursor.fetchall()

        if len(result) == 0:
            logger.warning(f"Student with sch_no {a} not found")
            print("Enter valid sch no.!")
        else:
            logger.info(f"Student with sch_no {a} found")
            for i in result:
                print(i)
    except Exception as e:
        logger.error(f"Error while searching for a student {a}: {e}", exc_info=True)
        print(f"Error searching student: {e}")

    input("Press Enter to continue!")


def update_student(cursor, conn):
    logger.info("Updating student data")

    print("------------------------")
    print("--- Update Student ---")
    print("------------------------")
    sch_no = input("Enter the sch no. of the student: ")
    name = input("Enter the name of the student: ")
    age = input("Enter the age of the student: ")
    email = input("Enter the email of the student: ")
    phone = input("Enter the phone no. of the student: ")

    logger.info(f"Updating student data with sch_no: {sch_no}")

    try:
        cursor.execute(
            "UPDATE studentsinfo SET name = ?, age = ?, email = ?, phone = ? WHERE sch_no = ?",
            (name, age, email, phone, sch_no)
        )

        if cursor.rowcount == 0:
            logger.warning(f"Student with sch_no {sch_no} not found for update")
            print("Student not found!")
        else:
            conn.commit()
            logger.info(f"Student {sch_no}'s data has been updated successfully.")
            print("Data updated successfully!")
    except Exception as e:
        logger.error(f"Error updating student {sch_no}: {e}", exc_info=True)
        print(f"Error updating data: {e}")

    input("Press Enter to continue!")


def delete_student(cursor, conn):
    logger.info("Removing a student")

    print("------------------------")
    print("--- Delete Student ---")
    print("------------------------")
    var1 = input("Enter the sch no. of the student: ")

    logger.info(f"Deleting a student from sch_no: {var1}")

    try:
        cursor.execute("DELETE FROM studentsinfo WHERE sch_no = ?", (var1,))

        if cursor.rowcount == 0:
            logger.warning(f"Student with sch_no {var1} not found for deletion")
            print("Student not found!")
        else:
            conn.commit()
            logger.info(f"Student with sch_no {var1} successfully removed")
            print("Data deleted successfully!")
    except Exception as e:
        logger.error(f"Error deleting student {var1}: {e}", exc_info=True)
        print(f"Error deleting data: {e}")

    input("Press Enter to continue!")
