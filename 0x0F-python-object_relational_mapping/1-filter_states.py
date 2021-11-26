#!/usr/bin/python3
"""
Script to list all states with a name starting with
N from the database hbtn_0e_0_usa.
Arguments recieved: mysql username, mysel password, database name
"""
from sys import argv
import MySQLdb

if __name__ == '__main__':
    # Open connection to database and get cursor
    database = MySQLdb.connect(host='localhost', port=3306,
                               user=argv[1], passwd=argv[2], db=argv[3])
    cursor = database.cursor()
    # Get info from table
    cursor.execute("SELECT states.id, states.name \
    FROM states WHERE states.name LIKE BINARY 'N%' ORDER BY id ASC")
    result = cursor.fetchall()
    # Print info
    for row in result:
        print(row)
    # Close connection to database and cursor
    cursor.close()
    database.close()
