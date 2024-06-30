#!/usr/bin/python3
import sys
import MySQLdb

def main():
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to MySQL
        db = MySQLdb.connect(host='localhost',
                             user=username,
                             passwd=password,
                             db=database,
                             port=3306)

        # Create a cursor object using cursor() method
        cursor = db.cursor()

        # Execute SQL query to fetch all states ordered by id
        cursor.execute("SELECT * FROM states ORDER BY id")

        # Fetch all rows using fetchall() method
        states = cursor.fetchall()

        # Print results as requested
        for state in states:
            print(state)

        # Disconnect from server
        db.close()

    except MySQLdb.Error as e:
        print("MySQLdb error:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()
