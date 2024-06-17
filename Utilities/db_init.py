import mysql.connector
import os
from dotenv import load_dotenv
from Utilities import db_functions

load_dotenv()
db_config = {
    'database': os.getenv('DB_DATABASE')
}

def initialize_db():
    connection = db_functions.connection()
    cursor = connection.cursor()

    # Check if the users table exists
    cursor.execute("""
    SELECT COUNT(*)
    FROM information_schema.tables
    WHERE table_schema = %s
    AND table_name = %s
    """, (db_config['database'], 'users'))

    if cursor.fetchone()[0] == 0:
        # Create the users table
        cursor.execute("""
        CREATE TABLE users (
            id INT AUTO_INCREMENT PRIMARY KEY,
            username VARCHAR(50) NOT NULL UNIQUE,
            password_hash VARCHAR(255) NOT NULL,
            salt VARCHAR(255) NOT NULL
        )
        """)
        # print("Table 'users' created successfully.")
    # else:
        # print("Table 'users' already exists.")
    
    connection.close()

    return True

if __name__ == "__main__":
    success = initialize_db()
    if success:
        print("Database initialization successful!")