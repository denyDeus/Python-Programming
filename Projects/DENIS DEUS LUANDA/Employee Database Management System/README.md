# Employee Database Management System

A modular Python console application designed to manage employee records using a **MySQL** database hosted locally via **XAMPP**. This application fulfills all core CRUD requirements, utilizing parameterized queries for security, explicit exception handling for stability, and strict user input validation.

---

## Features

- **Add Employee Records:** Validates and inserts new records (`Name`, `Department`, and `Salary`) into the database.
- **Display All Employees:** Fetches and outputs all stored records in a clean, formatted table layout.
- **Update Employee Details:** Updates specific fields for an existing employee by their unique ID, allowing fields to remain unchanged if left blank.
- **Delete Records:** Safely removes an employee record from the database after verifying the ID exists.
- **Search Employees:** Queries the database using wildcards (`LIKE` operator) to find partial matches across both `Name` and `Department` fields.

---

## Technical Concepts Covered

- **Database Connectivity:** Established locally using `mysql-connector-python` to communicate with XAMPP's MySQL/MariaDB database server.
- **CRUD Operations:** Complete functional breakdown of Create, Read, Update, and Delete actions.
- **SQL Parameterization:** Protects against SQL Injection attacks by binding parameters to `%s` placeholders instead of concatenating strings.
- **Modular Programming:** Separates code into independent, functional components for scalability and readability.
- **Exception Handling:** Implements structural `try...except...finally` blocks to catch network errors (`mysql.connector.Error`) and data parsing faults (`ValueError`), guaranteeing that database connections close reliably under all conditions.

---

## Database Schema

### Table Name: `Employees`

| Field Name | Data Type | Key / Extra | Description |
| :--- | :--- | :--- | :--- |
| **EmployeeID** | INT | PRIMARY KEY, AUTO_INCREMENT | Unique identifier for each employee |
| **Name** | VARCHAR(100) | NOT NULL | Full name of the employee |
| **Department**| VARCHAR(50)  | NOT NULL | Assigned department name |
| **Salary** | DECIMAL(10,2)| NOT NULL | Employee salary amount |

---
