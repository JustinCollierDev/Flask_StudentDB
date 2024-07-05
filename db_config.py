import os
import mysql.connector
from urllib.parse import urlparse

def get_db_connection():
    db_url = os.environ.get('JAWSDB_URL')  # Fetch JAWSDB_URL from environment variables
    if db_url:
        url = urlparse(db_url)
        connection = mysql.connector.connect(
            host=url.hostname,
            user=url.username,
            password=url.password,
            database=url.path[1:],
            port=url.port
        )
        return connection
    else:
        # handle error if connectiong can't be made
        raise Exception('JAWSDB_URL not found in environment variables')

