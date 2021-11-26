#!/usr/bin/python3
"""
Script to list all cities from database hbtn_0e_0_usa.
Arguments taken: mysql username, mysql password, database name
"""
if __name__ == "__main__":
    # Import modules
    from sys import argv
    import MySQLdb
    # Open connection to database and get cursor
    database = MySQLdb.connect(host='localhost', port=3306, user=argv[1],
                               passwd=argv[2], db=argv[3])
    cursor = database.cursor()
    # Get info requested
    cursor.execute("SELECT cities.id, cities.name, states.name \
    FROM states INNER JOIN cities \
    WHERE cities.state_id = states.id ORDER BY cities.id ASC")
    results = cursor.fetchall()
    # Print info
    for row in results:
        print(row)
    # Close connection to database and cursor
    cursor.close()
    database.close()
