import mysql.connector
from mysql.connector import Error
import os
from dotenv import load_dotenv

# DB Connection Configuration
load_dotenv()

db_config = {
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_DATABASE')
}

def connect_to_mariadb():
    connection = None
    try:
        connection = mysql.connector.connect(**db_config)

        if connection.is_connected():
            db_info = connection.get_server_info()
            cursor = connection.cursor()
            cursor.execute("select database();")
            record = cursor.fetchone()
            return True

    except Error as e:
        return False

    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

if __name__ == "__main__":
    success = connect_to_mariadb()
    if success:
        print("Connection Successful!")
    else:
        print("Connection Failed!")