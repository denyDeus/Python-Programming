from database import Database

class Student:

    def __init__(self):
        self.db = Database()

    def register(self):

        fullname = input("Enter Full Name: ")
        username = input("Enter Username: ")
        password = input("Enter Password: ")

        connection = self.db.connect()

        if connection:

            cursor = connection.cursor()

            try:

                cursor.execute(
                    "SELECT * FROM students WHERE username=%s",
                    (username,)
                )

                existing_user = cursor.fetchone()

                if existing_user:
                    print("Username already exists.")
                    return

                cursor.execute(
                    """
                    INSERT INTO students
                    (fullname, username, password)
                    VALUES (%s, %s, %s)
                    """,
                    (fullname, username, password)
                )

                connection.commit()

                print("Registration Successful!")

            except Exception as e:
                print("Error:", e)

            finally:
                cursor.close()
                connection.close()

    def login(self):

        username = input("Enter Username: ")
        password = input("Enter Password: ")

        connection = self.db.connect()

        if connection:

            cursor = connection.cursor()

            try:

                cursor.execute(
                    """
                    SELECT * FROM students
                    WHERE username=%s AND password=%s
                    """,
                    (username, password)
                )

                user = cursor.fetchone()

                if user:
                    print("Login Successful!")
                    print(f"Welcome {user[1]}")

                    self.student_menu(user[0])

                else:
                    print("Invalid Username or Password")

            except Exception as e:
                print("Error:", e)

            finally:
                cursor.close()
                connection.close()

    def student_menu(self, student_id):

        while True:

            print("\n===== STUDENT MENU =====")
            print("1. View Courses")
            print("2. Enroll Course")
            print("3. View My Courses")
            print("4. Logout")

            choice = input("Choose option: ")

            if choice == "1":
                self.view_courses()

            elif choice == "2":
                self.enroll_course(student_id)

            elif choice == "3":
                self.view_my_courses(student_id)

            elif choice == "4":
                print("Logged out successfully.")
                break

            else:
                print("Invalid option.")

    def view_courses(self):

        connection = self.db.connect()

        if connection:

            cursor = connection.cursor()

            cursor.execute("SELECT * FROM courses")

            courses = cursor.fetchall()

            print("\nAVAILABLE COURSES")

            for course in courses:
                print(
                    f"ID: {course[0]} | "
                    f"{course[1]} | "
                    f"{course[2]}"
                )

            cursor.close()
            connection.close()

    def enroll_course(self, student_id):

        self.view_courses()

        try:
            course_id = int(input("\nEnter Course ID: "))

            connection = self.db.connect()

            if connection:

                cursor = connection.cursor()

                cursor.execute(
                    """
                    SELECT * FROM enrollments
                    WHERE student_id=%s AND course_id=%s
                    """,
                    (student_id, course_id)
                )

                existing = cursor.fetchone()

                if existing:
                    print("You are already enrolled in this course.")

                else:

                    cursor.execute(
                        """
                        INSERT INTO enrollments
                        (student_id, course_id)
                        VALUES (%s, %s)
                        """,
                        (student_id, course_id)
                    )

                    connection.commit()

                    print("Course enrolled successfully!")

                cursor.close()
                connection.close()

        except ValueError:
            print("Please enter a valid Course ID.")

    def view_my_courses(self, student_id):

        connection = self.db.connect()

        if connection:

            cursor = connection.cursor()

            cursor.execute(
                """
                SELECT courses.course_name,
                    courses.course_code
                FROM courses
                JOIN enrollments
                ON courses.course_id = enrollments.course_id
                WHERE enrollments.student_id=%s
                """,
                (student_id,)
            )

            courses = cursor.fetchall()

            print("\nMY COURSES")

            if courses:

                for course in courses:

                    print(
                        f"{course[0]} ({course[1]})"
                    )

            else:
                print("No enrolled courses found.")

            cursor.close()
            connection.close()