import pymysql

# Replace with your MySQL connection details
DB_HOST = 'hirenation-victorjayeoba02.b.aivencloud.com'
DB_PORT = 14908  # PyMySQL uses integer for the port
DB_USER = 'avnadmin'
DB_PASSWORD = 'AVNS_Tv3zVYivwWC6fPeakvw'
DB_NAME = 'defaultdb'

try:
    print("Starting connection to the database...")

    # Establish a connection to MySQL using PyMySQL
    connection = pymysql.connect(
        host=DB_HOST,
        port=DB_PORT,
        user=DB_USER,
        password=DB_PASSWORD,
        database=DB_NAME,
        connect_timeout=10  # Timeout in seconds
    )

    print("Connection established successfully.")

    # Check if the connection is valid
    if connection.open:
        print("Connection to MySQL database confirmed.")

        # Create a cursor object
        print("Creating cursor...")
        cursor = connection.cursor()

        # Execute a query to fetch data from the database
        print("Executing query to fetch data...")
        cursor.execute("SELECT * FROM jobs;")  # Replace 'your_table_name' with the actual table name
        
        # Fetch all rows of the query result
        results = cursor.fetchall()
        print(f"Query executed successfully. {len(results)} rows fetched.")

        # Print each row from the results
        print("Data from the database:")
        for row in results:
            print(row)

        # Close the cursor and connection
        cursor.close()
        connection.close()

        print("Connection and cursor closed.")
    
    else:
        print("Unable to confirm connection.")

except pymysql.MySQLError as err:
    print(f"An error occurred during connection or query execution: {err}")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    # Ensure that connection is closed properly even if an error occurred
    try:
        if connection.open:
            connection.close()
            print("Connection closed.")
    except NameError:
        pass  # In case the connection object was never initialized
