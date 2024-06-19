from Utilities import db_functions
from argon2 import PasswordHasher

def loginUser(username, password):
    connection = db_functions.connection()
    cursor = connection.cursor()

    cursor.execute("SELECT password_hash FROM users WHERE username = %s", (username,))

    result = cursor.fetchone()
    connection.close()

    ph = PasswordHasher() 

    if result:
        stored_hashed = result[0]

        # verify hash
        if ph.verify(stored_hashed, password):
            print("Login successful!")
        else:
            print("Incorrect password. Please try again.")
    else:
        print("User not found. Please register...")