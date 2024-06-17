import mysql.connector
from dotenv import load_dotenv
import os

# DB Connection Configuration
load_dotenv()

db_config = {
    'user': os.getenv('DB_USERNAME'),
    'password': os.getenv('DB_PASSWORD'),
    'host': os.getenv('DB_HOST'),
    'database': os.getenv('DB_DATABASE')
}

def connection():
    try:
        myDB = mysql.connector.connect(**db_config)
        return myDB
    except mysql.connector.Error as err:
        print("Error connecting to database! See: ", err)