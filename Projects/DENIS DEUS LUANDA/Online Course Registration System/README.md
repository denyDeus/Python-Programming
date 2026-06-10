# Online Course Registration System

## Overview
This is a console-based Online Course Registration System built using Python and MySQL. It allows students to register, log in, and enroll in courses, while administrators can manage users and course data through a terminal interface.

## Features
- Student registration and login
- Admin login and management panel
- Course registration and enrollment
- MySQL database integration
- Simple command-line interface (CLI)

## Technologies Used
- Python
- MySQL
- MySQL Connector for Python

## Installation

1. Clone the repository:
git clone https://github.com/your-username/online-course-registration.git

2. Install dependencies:
pip install mysql-connector-python

3. Set up MySQL database:
- Create a database (e.g. course_registration)
- Import your SQL file if available

4. Update database configuration in your Python file:
host = "localhost"
user = "root"
password = "your_password"
database = "course_registration"

## How to Run
Run the program using:
python main.py

## Project Structure
- main.py
- database.py
- auth.py
- courses.py
- students.py
- README.md

## Future Improvements
- Add graphical user interface (GUI)
- Improve password security using hashing
- Add email notifications
- Convert to web-based system using Flask or Django
