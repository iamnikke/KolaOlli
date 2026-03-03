import mysql.connector
from mysql.connector import errorcode
import os

DB_USER = 'sun db käyttäjä'
DB_PASSWORD = 'sun db salasana'
DB_HOST = 'sun db host'
DB_NAME = 'tietokannan nimi'
SQL_FILE = 'db.sql'


def create_database_from_sql():
    # yhdistää mariadb serveriin
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()
        print("Connected to MariaDB server.")

        # luo tietokannan
        try:
            cursor.execute(f"CREATE DATABASE {DB_NAME} DEFAULT CHARACTER SET 'utf8mb4'")
            print(f"Database '{DB_NAME}' created.")
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_DB_CREATE_EXISTS:
                print(f"Database '{DB_NAME}' already exists.")
            else:
                print(f"Failed creating database: {err}")
                exit(1)

        cursor.close()
        conn.close()

    except mysql.connector.Error as err:
        print(f"Error connecting to MariaDB: {err}")
        exit(1)

    # avaa luodun databasen ja syöttää dump filen
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = conn.cursor()

        # Check if file exists
        if not os.path.exists(SQL_FILE):
            print(f"Error: SQL file '{SQL_FILE}' not found.")
            return

        print(f"Reading and executing {SQL_FILE}...")

        # Read the file content
        with open(SQL_FILE, 'r', encoding='utf-8') as f:
            sql_data = f.read()

        # Splitaa dump filen yksittäisiin toimintoihin jotka ajetaan
        statements = sql_data.split(';')

        for statement in statements:
            if statement.strip():
                try:
                    cursor.execute(statement)
                except mysql.connector.Error as err:
                    print(f"Skipping statement due to error: {err}")

        conn.commit()
        print("SQL dump imported successfully.")

    except mysql.connector.Error as err:
        print(f"Error connecting to database '{DB_NAME}': {err}")
    finally:
        if conn.is_connected():
            cursor.close()
            conn.close()
            print("MariaDB connection closed.")


create_database_from_sql()