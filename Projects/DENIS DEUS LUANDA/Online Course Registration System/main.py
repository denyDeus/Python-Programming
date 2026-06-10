from student import Student
from admin import Admin

student = Student()
admin = Admin()

while True:

    print("\n===== ONLINE COURSE REGISTRATION SYSTEM =====")
    print("1. Register")
    print("2. Student Login")
    print("3. Admin Login")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        student.register()

    elif choice == "2":
        student.login()

    elif choice == "3":
        admin.login()

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option.")