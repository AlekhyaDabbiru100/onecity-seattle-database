import os
import mysql.connector
from mysql.connector import Error

DB_CONFIG = {
    "host": os.getenv("DB_HOST", "cssql.seattleu.edu"),
    "user": os.getenv("DB_USER", "your_username"),
    "password": os.getenv("DB_PASSWORD", "your_password"),
    "database": os.getenv("DB_NAME", "your_database_name"),
    "use_pure": True
}


def get_connection():
    """
    Creates and returns a MySQL database connection.
    """
    try:
        connection = mysql.connector.connect(**DB_CONFIG)

        if connection.is_connected():
            return connection

    except Error as error:
        raise ConnectionError(f"Database connection failed: {error}")

    return None


def run_query(query):
    """
    Runs a SQL query and returns column names + rows.
    """
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute(query)

        rows = cursor.fetchall()
        columns = [description[0] for description in cursor.description]

        return columns, rows

    except Error as error:
        raise RuntimeError(f"SQL query failed: {error}")

    finally:
        if cursor:
            cursor.close()

        if connection and connection.is_connected():
            connection.close()