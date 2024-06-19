import bcrypt
from Utilities import db_functions

def login(username, password):
    connection = db_functions.connection()
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