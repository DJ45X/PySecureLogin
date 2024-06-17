import mysql.connector
import os
from dotenv import load_dotenv
import bcrypt

# DB Connection Configuration
load_dotenv()

db_config = {
    'host': '192.168.0.110',
    'database': 'pySecureDB',
    'user': 'TestUserDB',
    'password': 'MyTestPassword',
}

def login(username, password):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor()
    cursor.execute("SELECT password_hash, salt FROM users WHERE username = %s", (username,))
    result = cursor.fetchone()
    connection.close()

    if result:
        stored_hashed_password, salt = result
        if bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
            print("Login successful!")
        else:
            print("Incorrect password. Please try again.")
    else:
        print("User not found. Please register...")