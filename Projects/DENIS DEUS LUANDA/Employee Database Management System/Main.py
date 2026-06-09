import mysql.connector
from mysql.connector import Error

def get_db_connection():
    """Establishes and returns a connection to the XAMPP MySQL database."""
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',       # Default XAMPP username
            password='',       # Default XAMPP password is empty
            database='company_db'
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# ==========================================
# FUNCTIONAL REQUIREMENTS (CRUD Operations)
# ==========================================

def add_employee():
    """Validates input and inserts a new employee record."""
    print("\n--- Add New Employee ---")
    name = input("Enter Name: ").strip()
    department = input("Enter Department: ").strip()
    
    # Input Validation for Salary
    try:
        salary = float(input("Enter Salary: "))
        if salary < 0:
            print("Salary cannot be negative.")
            return
    except ValueError:
        print("Invalid input. Salary must be a number.")
        return

    if not name or not department:
        print("Name and Department cannot be empty.")
        return

    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "INSERT INTO Employees (Name, Department, Salary) VALUES (%s, %s, %s)"
            cursor.execute(query, (name, department, salary))
            conn.commit()
            print(f"Success: Employee record added successfully!")
        except Error as e:
            print(f"Database Error: {e}")
        finally:
            cursor.close()
            conn.close()

def display_all_employees():
    """Fetches and displays all records from the table."""
    print("\n--- All Employee Records ---")
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM Employees")
            records = cursor.fetchall()
            
            if not records:
                print("No records found.")
                return

            print(f"{'ID':<5} | {'Name':<20} | {'Department':<15} | {'Salary':<10}")
            print("-" * 60)
            for row in records:
                print(f"{row[0]:<5} | {row[1]:<20} | {row[2]:<15} | ${row[3]:.2f}")
        except Error as e:
            print(f"Database Error: {e}")
        finally:
            cursor.close()
            conn.close()

def update_employee():
    """Updates an employee's details based on their ID."""
    print("\n--- Update Employee Details ---")
    try:
        emp_id = int(input("Enter the Employee ID to update: "))
    except ValueError:
        print("Invalid ID. Must be an integer.")
        return

    # Prompting for new details
    new_name = input("Enter new Name (leave blank to keep current): ").strip()
    new_dept = input("Enter new Department (leave blank to keep current): ").strip()
    new_salary_input = input("Enter new Salary (leave blank to keep current): ").strip()

    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            
            # First, check if the employee exists
            cursor.execute("SELECT * FROM Employees WHERE EmployeeID = %s", (emp_id,))
            current_data = cursor.fetchone()
            if not current_data:
                print("Employee ID not found.")
                return

            # Fallback to existing data if fields are left blank
            name = new_name if new_name else current_data[1]
            department = new_dept if new_dept else current_data[2]
            salary = float(new_salary_input) if new_salary_input else current_data[3]

            query = "UPDATE Employees SET Name = %s, Department = %s, Salary = %s WHERE EmployeeID = %s"
            cursor.execute(query, (name, department, salary, emp_id))
            conn.commit()
            print("Success: Employee details updated successfully!")
        except ValueError:
            print("Invalid salary amount. Update cancelled.")
        except Error as e:
            print(f"Database Error: {e}")
        finally:
            cursor.close()
            conn.close()

def delete_employee():
    """Deletes an employee record by ID."""
    print("\n--- Delete Employee Record ---")
    try:
        emp_id = int(input("Enter Employee ID to delete: "))
    except ValueError:
        print("Invalid ID.")
        return

    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            # Check if record exists
            cursor.execute("SELECT * FROM Employees WHERE EmployeeID = %s", (emp_id,))
            if not cursor.fetchone():
                print("Employee ID not found.")
                return

            query = "DELETE FROM Employees WHERE EmployeeID = %s"
            cursor.execute(query, (emp_id,))
            conn.commit()
            print("Success: Employee deleted successfully!")
        except Error as e:
            print(f"Database Error: {e}")
        finally:
            cursor.close()
            conn.close()

def search_employees():
    """Searches for employees by Name or Department using SQL LIKE keyword."""
    print("\n--- Search Employees ---")
    search_term = input("Enter Name or Department to search for: ").strip()
    
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM Employees WHERE Name LIKE %s OR Department LIKE %s"
            # Using % wildcards allows matching partial strings
            wildcard_term = f"%{search_term}%"
            cursor.execute(query, (wildcard_term, wildcard_term))
            records = cursor.fetchall()

            if not records:
                print("No matching employees found.")
                return

            print(f"\n{'ID':<5} | {'Name':<20} | {'Department':<15} | {'Salary':<10}")
            print("-" * 60)
            for row in records:
                print(f"{row[0]:<5} | {row[1]:<20} | {row[2]:<15} | ${row[3]:.2f}")
        except Error as e:
            print(f"Database Error: {e}")
        finally:
            cursor.close()
            conn.close()

# ==========================================
# MENU INTERFACE
# ==========================================

def main_menu():
    """The main interface loop providing application navigation."""
    while True:
        print("\n==================================")
        print(" EMPLOYEE DATABASE MANAGEMENT     ")
        print("==================================")
        print("1. Add Employee")
        print("2. Display All Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Search Employees")
        print("6. Exit")
        
        choice = input("Select an option (1-6): ").strip()
        
        if choice == '1':
            add_employee()
        elif choice == '2':
            display_all_employees()
        elif choice == '3':
            update_employee()
        elif choice == '4':
            delete_employee()
        elif choice == '5':
            search_employees()
        elif choice == '6':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid selection. Please choose a number between 1 and 6.")

if __name__ == "__main__":
    main_menu()