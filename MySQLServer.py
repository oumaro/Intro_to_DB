import mysql.connector
from mysql.connector import Error

# Replace with your actual MySQL credentials
DB_HOST = "localhost"
DB_USER = "your_mysql_user"  # e.g., "root"
DB_PASSWORD = "your_mysql_password"
DB_NAME = "alx_book_store"

def create_database():
    """Connects to MySQL and creates the specified database if it doesn't exist."""
    connection = None
    try:
        # Establish connection to the MySQL server (without specifying a database initially)
        connection = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # SQL command to create the database if it does not exist
            # This prevents the script from failing if the database already exists
            create_db_query = f"CREATE DATABASE IF NOT EXISTS {DB_NAME}"

            # Execute the query
            cursor.execute(create_db_query)
            
            # Print the success message
            print(f"Database '{DB_NAME}' created successfully!")

    except Error as e:
        # Handle connection errors (e.g., incorrect credentials, server down)
        print(f"Error connecting to MySQL or creating the database: {e}")

    finally:
        # Close the cursor and connection to ensure resources are released
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed.") # Optional: Confirmation of close

if __name__ == '__main__':
    # ⚠️ IMPORTANT: Update DB_USER and DB_PASSWORD before running!
    create_database()
