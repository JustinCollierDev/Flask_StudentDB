import os
import mysql.connector
from urllib.parse import urlparse

def get_db_connection():
    db_url = os.environ.get('mysql://w2xyawpti7k8bp70:ujow0ny034la0elg@o3iyl77734b9n3tg.cbetxkdyhwsb.us-east-1.rds.amazonaws.com:3306/c1obmzcccmpqz8pq') #JAWSBD url used for Heroku deployment
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
        # Fallback to local database configuration
        connection = mysql.connector.connect(
        host='localhost',
        user='root',
        password='root',
        database='student_db'
    )
    return connection
