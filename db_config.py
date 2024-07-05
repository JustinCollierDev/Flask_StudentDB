import os
import mysql.connector
from urllib.parse import urlparse
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_db_connection():
    db_url = os.environ.get('JAWSDB_URL')  # Fetch JAWSDB_URL from environment variables
    print(f"DEBUG: db_url={db_url}")

    if not db_url:
        raise Exception('JAWSDB_URL not found in environment variables')

    if db_url:
        url = urlparse(db_url)
        print(f"DEBUG: url={url}")
        connection = mysql.connector.connect(
            host=url.hostname,
            user=url.username,
            password=url.password,
            database=url.path[1:],
            port=url.port
        )
        # Check if 'students' table exists, create if not
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS students (
                student_id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                first_name VARCHAR(50),
                last_name VARCHAR(50),
                dob DATE,
                amount_due DECIMAL(10, 2)
            )
        """)
        cursor.close()
        return connection
    else:
        raise Exception('JAWSDB_URL not found in environment variables')

# Debugging statement to verify environment variables
print(f"DEBUG: JAWSDB_URL={os.environ.get('JAWSDB_URL')}")
