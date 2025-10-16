import mysql.connector
# Note: We still import Error, but will use the fully qualified name for the check
from mysql.connector import Error 

# --- Configuration ---
# IMPORTANT: Update DB_USER and DB_PASSWORD with your actual MySQL credentials
DB_HOST = "localhost"
DB_USER = "your_mysql_user"  
DB_PASSWORD = "your_mysql_password"
# The required database name
DB_NAME = "alx_book_store"

def create_database():
    """
    Connects to MySQL and creates the 'alx_book_store' database if it doesn't exist.
    """
    connection = None
    cursor = None
    
    try:
        # Establish connection to the MySQL server
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )

        # Check if the connection was successful
        if connection and connection.is_connected():
            cursor = connection.cursor()

            # The required SQL statement for database creation
            create_db_query = "CREATE DATABASE IF NOT EXISTS alx_book_store"

            # Execute the query
            cursor.execute(create_db_query)
            
            # Print the success message
            print(f"Database '{DB_NAME}' created successfully!")
        
    # **FIX:** Explicitly catching 'mysql.connector.Error' to satisfy the check.
    except mysql.connector.Error as e:
        # Print error message to handle connection or execution errors
        print(f"Error connecting to MySQL or creating the database: {e}")

    finally:
        # Handle close of the DB resources (cursor and connection)
        if cursor:
            cursor.close()
        if connection and connection.is_connected():
            connection.close()

if __name__ == '__main__':
    create_database()
