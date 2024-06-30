#!/usr/bin/python3
import sys
import MySQLdb

if __name__ == "__main__":
    # Command line arguments: username, password, database name
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    # Create a cursor object using cursor() method
    cursor = db.cursor()

    # SQL query to retrieve all states sorted by id
    sql_query = "SELECT * FROM states ORDER BY id ASC"

    try:
        # Execute the SQL command
        cursor.execute(sql_query)
        # Fetch all the rows in a list of tuples
        results = cursor.fetchall()
        # Print each row
        for row in results:
            print(row)
    except MySQLdb.Error as e:
        print(f"Error executing the query: {e}")

    # Disconnect from server
    db.close()
