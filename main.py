from Utilities import db_connection_test, db_init
from Cogs import register, login
import re

def main():
    while True:
        print("[1] - Register a new user")
        print("[2] - Login")
        print("[3] - Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            username = input("Enter username: ")
            password = input("Enter password: ")

            username_regex = r'^[a-zA-Z0-9_]{3,20}$'
            while not re.match(username_regex, username):
                print("Username must be between 3 and 20 characters long and can only contain letters, numbers, and underscores")
                username = input("Enter username: ")

            # Sanitize user input
            username = username.strip()
            
            register.registerUser(username, password)

        elif choice == "2":
            username = input("Enter username: ")
            password = input("Enter password: ")

            username_regex = r'^[a-zA-Z0-9_]{3,20}$'
            # validate username
            while not re.match(username_regex, username):
                print("Username must be between 3 and 20 characters long and can only contain letters, numbers, and underscores")
                username = input("Enter username: ")
            # Sanitize user input
            username = username.strip()

            login.loginUser(username, password)
            
        elif choice == "3":
            break
        else:
            print("Invalid choice. Please try again.")

def connection_test():
    success = db_connection_test.connect_to_mariadb()
    if success:
        check_table_exists = db_init.initialize_db()
        if check_table_exists:
            main()
    else:
        print("Connection Failed! Exiting program...")
        exit()

if __name__ == "__main__":
    connection_test() # Comment this line and uncomment main() to run without db_connection_test and db_init
    # main()