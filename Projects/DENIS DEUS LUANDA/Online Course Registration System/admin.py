from database import Database

class Admin:

    def __init__(self):
        self.db = Database()

    def login(self):

        username = input("Admin Username: ")
        password = input("Admin Password: ")

        if username == "admin" and password == "12345":
            print("Admin Login Successful!")
            self.admin_menu()

        else:
            print("Invalid Admin Credentials")

    def admin_menu(self):

        while True:

            print("\n===== ADMIN MENU =====")
            print("1. Add Course")
            print("2. Delete Course")
            print("3. View Students")
            print("4. Generate Report")
            print("5. Logout")

            choice = input("Choose option: ")

            if choice == "1":
                self.add_course()

            elif choice == "2":
                self.delete_course()

            elif choice == "3":
                self.view_students()

            elif choice == "4":
                self.generate_report()

            elif choice == "5":
                print("Admin Logged Out")
                break

            else:
                print("Invalid Option")

    def add_course(self):

        course_name = input("Enter Course Name: ")
        course_code = input("Enter Course Code: ")

        connection = self.db.connect()

        if connection:

            cursor = connection.cursor()

            try:

                cursor.execute(
                    """
                    INSERT INTO courses
                    (course_name, course_code)
                    VALUES (%s, %s)
                    """,
                    (course_name, course_code)
                )

                connection.commit()

                print("Course Added Successfully!")

            except Exception as e:
                print("Error:", e)

            finally:
                cursor.close()
                connection.close()

    def delete_course(self):

        course_id = input("Enter Course ID to delete: ")

        connection = self.db.connect()

        if connection:

            cursor = connection.cursor()

            try:

                cursor.execute(
                    "DELETE FROM courses WHERE course_id=%s",
                    (course_id,)
                )

                connection.commit()

                print("Course deleted successfully!")

            except Exception as e:
                print("Error:", e)

            finally:
                cursor.close()
                connection.close()

    def view_students(self):

        connection = self.db.connect()

        if connection:

            cursor = connection.cursor()

            try:

                cursor.execute(
                    """
                    SELECT student_id,
                        fullname,
                        username
                    FROM students
                    """
                )

                students = cursor.fetchall()

                print("\n===== STUDENTS =====")

                for student in students:
                    print(
                        f"ID: {student[0]} | "
                        f"Name: {student[1]} | "
                        f"Username: {student[2]}"
                    )

            except Exception as e:
                print("Error:", e)

            finally:
                cursor.close()
                connection.close()

    def generate_report(self):

        connection = self.db.connect()

        if connection:

            cursor = connection.cursor()

            try:

                cursor.execute(
                    """
                    SELECT students.fullname,
                        courses.course_name,
                        courses.course_code
                    FROM enrollments
                    JOIN students
                        ON enrollments.student_id = students.student_id
                    JOIN courses
                        ON enrollments.course_id = courses.course_id
                    """
                )

                records = cursor.fetchall()

                print("\n===== ENROLLMENT REPORT =====")

                if records:

                    for record in records:

                        print(
                            f"{record[0]} | "
                            f"{record[1]} | "
                            f"{record[2]}"
                        )

                else:
                    print("No enrollments found.")

            except Exception as e:
                print("Error:", e)

            finally:
                cursor.close()
                connection.close()