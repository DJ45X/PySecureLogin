import mysql.connector
from argon2 import PasswordHasher, low_level
from Utilities import db_functions
import re
from dotenv import load_dotenv
from os import getenv

# load environment variables
load_dotenv()

def validate_password(password):
    # Define the password requirements
    min_length = 8
    lowercase_patter = re.compile(r'[a-z]')
    uppercase_patter = re.compile(r'[A-Z]')
    number_pattern = re.compile(r'\d')
    special_char_pattern = re.compile(r'[!@#$%^&*(),.?":{}|<>]')

    # check each requirement
    if len(password) < min_length:
        return False, "Password must be at least 8 characters long."
    if not lowercase_patter.search(password):
        return False, "Password must contain at least one lowercase letter."
    if not uppercase_patter.search(password):
        return False, "Password must contain at least one uppercase letter."
    if not number_pattern.search(password):
        return False, "Password must contain at least one number."
    if not special_char_pattern.search(password):
        return False, "Password must contain at least one special character."

    return True, "Password is valid."

def registerUser(username, password):
    is_valid, message = validate_password(password)
    if not is_valid:
        print(f"Password validation failed: {message}")
        return

    # get the pepper
    pepper = getenv('PEPPER')
    if not pepper:
        raise ValueError("Pepper environment variable not set")

    # concat the password and pepper
    peppered_password = password + pepper

    connection = db_functions.connection()
    cursor = connection.cursor()

    ph = PasswordHasher(
        time_cost=1,
        memory_cost=1048576,
        parallelism=4,
        hash_len=32,
        type=low_level.Type.ID,
        salt_len=16
    )
    
    hashed_password = ph.hash(peppered_password)

    with db_functions.connection() as connection:
        with connection.cursor() as cursor:
            try:
                cursor.execute("INSERT INTO users (username, password_hash) VALUES (%s, %s)", (username, hashed_password))
                connection.commit()
                print("User Registered Successfully!")
            except mysql.connector.errors.IntegrityError:
                print("User already exists!")
            finally:
                connection.close()