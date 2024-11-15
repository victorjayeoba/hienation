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
        port=int(os.getenv('MYSQL_PORT')),
        password=os.getenv('MYSQL_PASSWORD'),
        db=os.getenv('MYSQL_DB'),
        connect_timeout=10  # Timeout in seconds    
        )
        return connection
    except pymysql.MySQLError as err:
        print(f"Error: {err}")
        return None


def convert_to_object(job):
    return {
        "id": job[0],
        "title": job[1],
        "location": job[2],
        "salary": job[3],
        "currency": job[4],
        "jobDescription": job[5],
        "qualifications": job[6],
        "exp_requirement": job[7]
    }

# Apply the function to each item in the list

def fetch_jobs():
    connection = create_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM jobs")
    jobs = cursor.fetchall()
    result = map(convert_to_object, jobs)
    connection.close()
    return list(result)

