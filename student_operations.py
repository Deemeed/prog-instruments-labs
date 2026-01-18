def add_student(cursor, conn):
    print("-------------------------")
    print("Add Student Information")
    print("-------------------------")
    var1 = input("Enter the sch no. of the student: ")
    var2 = input("Enter the name of the student: ")
    var3 = input("Enter the age of the student: ")
    var4 = input("Enter the email of the student: ")
    var5 = input("Enter the phone no. of the student: ")

    cursor.execute(
        "INSERT INTO studentsinfo VALUES (?, ?, ?, ?, ?)",
        (var1, var2, var3, var4, var5)
    )
    conn.commit()
    print("Data saved successfully!")
    input("Press Enter to continue!")


def view_students(cursor):
    print("------------------------")
    print("--- Student Records ---")
    print("------------------------")
    cursor.execute("SELECT * FROM studentsinfo")
    for i in cursor:
        print(i)
    input("Press Enter to continue!")


def search_student(cursor):
    print("------------------------")
    print("--- Search Student ---")
    print("------------------------")
    a = input("Enter the sch no. of the student:")

    cursor.execute("SELECT * FROM studentsinfo WHERE sch_no = ?", (a,))
    result = cursor.fetchall()

    if len(result) == 0:
        print("Enter valid sch no.!")
    else:
        for i in result:
            print(i)
    input("Press Enter to continue!")


def update_student(cursor, conn):
    print("------------------------")
    print("--- Update Student ---")
    print("------------------------")
    sch_no = input("Enter the sch no. of the student: ")
    name = input("Enter the name of the student: ")
    age = input("Enter the age of the student: ")
    email = input("Enter the email of the student: ")
    phone = input("Enter the phone no. of the student: ")

    cursor.execute(
        "UPDATE studentsinfo SET name = ?, age = ?, email = ?, phone = ? WHERE sch_no = ?",
        (name, age, email, phone, sch_no)
    )
    conn.commit()
    print("Data updated successfully!")
    input("Press Enter to continue!")


def delete_student(cursor, conn):
    print("------------------------")
    print("--- Delete Student ---")
    print("------------------------")
    var1 = input("Enter the sch no. of the student:")
    cursor.execute("DELETE FROM studentsinfo WHERE sch_no = ?", (var1,))
    conn.commit()
    print("Data deleted successfully!")
    input("Press Enter to continue!")
