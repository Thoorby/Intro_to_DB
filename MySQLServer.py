import mysql.connector
from mysql.connector import errorcode

def create_database():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",          # Change to your MySQL user if needed
            password="your_password"  # Change to your MySQL password
        )
        cursor = conn.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")
    except mysql.connector.Error as err:
        print(f"Error: Could not connect or create database. {err}")
    finally:
        try:
            cursor.close()
        except:
            pass
        try:
            conn.close()
        except:
            pass

if __name__ == "__main__":
    create_database()
