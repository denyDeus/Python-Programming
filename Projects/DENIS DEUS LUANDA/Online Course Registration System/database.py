import mysql.connector
from config import DB_CONFIG


class Database:

    def connect(self):
        try:
            connection = mysql.connector.connect(**DB_CONFIG)
            return connection

        except Exception as e:
            print("Database Error:", e)
            return None