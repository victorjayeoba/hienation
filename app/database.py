import pymysql
import os
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

# Function to create a MySQL connection
def create_db_connection():
    try:
        connection = pymysql.connect(
        host=os.getenv('MYSQL_HOST'),
        user=os.getenv('MYSQL_USER'),
        port=14908,
        password=os.getenv('MYSQL_PASSWORD'),
        db=os.getenv('MYSQL_DB'),
        connect_timeout=10  # Timeout in seconds    
        )
        return connection
    except pymysql.MySQLError as err:
        print(f"Error: {err}")
        return None


def fetch_jobs():
    connection = create_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()
    connection.close()
    return jobs
