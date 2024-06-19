from Utilities import db_functions
from argon2 import PasswordHasher
from os import getenv
from dotenv import load_dotenv

load_dotenv()

def loginUser(username, password):
    connection = db_functions.connection()
    cursor = connection.cursor()

    try:
        query = "SELECT password_hash FROM users WHERE username = %s"
        cursor.execute(query, (username,))
        result = cursor.fetchone()

        if result:
            pepper = getenv('PEPPER')
            if not pepper:
                raise ValueError("Pepper environment variable not set")
            
            # concat password with pepper
            peppered_password = password + pepper

            # initialize the password hasher
            ph = PasswordHasher()

            # verify the hash directly without storing it
            if ph.verify(result[0], peppered_password):
                print("Login successful!")
            else:
                print("Incorrect password. Please try again.")
        else:
            print("User not found. Please register...")
    finally:
        cursor.close()
        connection.close()