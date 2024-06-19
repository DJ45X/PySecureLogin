from Utilities import db_functions
from argon2 import PasswordHasher
from os import getenv
from dotenv import load_dotenv

load_dotenv()

def loginUser(username, password):
    connection = db_functions.connection()
    cursor = connection.cursor()

    cursor.execute("SELECT password_hash FROM users WHERE username = %s", (username,))

    result = cursor.fetchone()
    connection.close()

    pepper = getenv('PEPPER')
    if not pepper:
        raise ValueError("Pepper environment variable not set")
    
    peppered_password = password + pepper

    ph = PasswordHasher() 

    if result:
        stored_hashed = result[0]

        # verify hash
        if ph.verify(stored_hashed, peppered_password):
            print("Login successful!")
        else:
            print("Incorrect password. Please try again.")
    else:
        print("User not found. Please register...")