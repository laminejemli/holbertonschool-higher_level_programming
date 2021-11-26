#!/usr/bin/python3
"""
Script to take the name of a state as an argumnet and list
all cities of that state using database hbtn_0e_4_usa.
Arguments taken: mysql username, mysql password, database name, state name
"""
if __name__ == "__main__":
    # Import necessary modules
    from sys import argv
    import MySQLdb
    # Open connection to database and make cursor
    database = MySQLdb.connect(host='localhost', port=3306,
                               user=argv[1], passwd=argv[2], db=argv[3])
    cursor = database.cursor()
    # Get the information
    cursor.execute("SELECT cities.name FROM cities \
    INNER JOIN states ON states.id = cities.state_id \
    WHERE states.name LIKE BINARY %s ORDER BY cities.id ASC", (argv[4], ))
    result = cursor.fetchall()
    # Print the inforamtion
    for i, row in enumerate(result):
        if i is not 0:
            print(", {:s}".format(row[0]), end='')
        else:
            print("{:s}".format(row[0]), end='')
    print()
    # Close connection to database and cursor
    cursor.close()
    database.close()
