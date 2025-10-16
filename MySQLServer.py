import mysql.connector
from mysql.connector import Error

# --- Configuration ---
# IMPORTANT: Update DB_USER and DB_PASSWORD with your actual MySQL credentials
DB_HOST = "localhost"
DB_USER = "your_mysql_user"  
DB_PASSWORD = "your_mysql_password"
# The required database name
DB_NAME = "alx_book_store"

def create_database():
    """Connects to MySQL and creates the 'alx_book_store' database if it doesn't exist."""
    connection = None
    cursor = None
    try:
        # Establish connection to the MySQL server (without specifying a database)
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )

        # Check if the connection was successful
        if connection.is_connected():
            cursor = connection.cursor()

            # SQL command to create the database IF NOT EXISTS
            # This ensures the script won't fail if 'alx_book_store' already exists.
            create_db_query = f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"

            # Execute the query
            cursor.execute(create_db_query)
            
            # Print the success message as required
            print(f"Database '{DB_NAME}' created successfully!")
        else:
            print("Failed to establish a connection to the MySQL server.")

    except Error as e:
        # Print error message to handle connection/execution errors
        print(f"Error connecting to MySQL or creating the database: {e}")

    finally:
        # Handle close of the DB resources
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()
            # print("MySQL connection is closed.") # Optional confirmation

if __name__ == '__main__':
    create_database()
