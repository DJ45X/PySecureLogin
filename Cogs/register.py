import mysql.connector
from argon2 import PasswordHasher
import argon2
from Utilities import db_functions

def registerUser(username, password):
    connection = db_functions.connection()
    cursor = connection.cursor()

    ph = PasswordHasher(
        time_cost=1,
        memory_cost=1048576,
        parallelism=4,
        hash_len=32,
        type=argon2.low_level.Type.ID,
        salt_len=16
    )
    
    hashed_password = ph.hash(password)

    try:
        cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (username, hashed_password))
        connection.commit()
        print("User Registered Successfully!")
    except mysql.connector.errors.IntegrityError:
        print("User already exists!")
    finally:
        connection.close()