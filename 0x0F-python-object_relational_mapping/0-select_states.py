#!/usr/bin/python3
"""Script to list all states from database hbtn_0e_0_usa.
Arguments received: mysql username, mysql password, database name
"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    """Get data from database"""
    database = MySQLdb.connect(host='localhost', port=3306,
                               user=argv[1], passwd=argv[2], db=argv[3])
    cursor = database.cursor()
    cursor.execute("SELECT states.id, states.name FROM states ORDER BY id ASC")
    result = cursor.fetchall()
    """Print results"""
    for row in result:
        print(row)
    """Close cursor and connection to database"""
    cursor.close()
    database.close()
