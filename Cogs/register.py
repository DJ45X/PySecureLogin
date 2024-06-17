import mysql.connector
import os
from dotenv import load_dotenv
import bcrypt
from Utilities import db_functions

def create_user(username, password):
    connection = db_functions.connection()
    cursor = connection.cursor()

    salt = bcrypt.gensalt().decode('utf-8')
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt.encode('utf-8')).decode('utf-8')

    try:
        cursor.execute("INSERT INTO users (username, password_hash, salt) VALUES (%s, %s, %s)", (username, hashed_password, salt))
        connection.commit()
        print("User Registered Successfully!")
    except mysql.connector.errors.IntegrityError:
        print("User already exists!")
    finally:
        connection.close()