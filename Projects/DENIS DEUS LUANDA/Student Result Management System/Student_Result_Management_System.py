# Student Result Management System

# Get Student Details
Student_Name = input("Enter Student Name: ")
Reg_Num = input("Enter Registration Number: ")

# Get Marks for 5 Subjects
def get_marks():
    marks = []

    for i in range(5):
        while True:
            try:
                mark = int(input(f"Enter Mark {i+1}: "))

                if mark < 0 or mark > 100:
                    print("Marks must be between 0 and 100")
                else:
                    marks.append(mark)
                    break

            except ValueError:
                print("Please enter a valid number")

    return marks

marks = get_marks()

# Calculate Total Marks
total = sum(marks)

# Calculate Average Marks
average = total / len(marks)

# Determine Grade
def calculate_grade(avg):
    if avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    else:
        return "F"

grade = calculate_grade(average)

print("\n===== STUDENT RESULT =====")
print("Student Name:", Student_Name)
print("Registration Number:", Reg_Num)
print("Marks:", marks)
print("Total Marks:", total)
print("Average Marks:", average)
print("Grade:", grade)