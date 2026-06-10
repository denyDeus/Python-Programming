import mysql.connector

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="course_registration"
    )

    if connection.is_connected():
        print("Database connected successfully!")

except Exception as e:
    print("Error:", e)