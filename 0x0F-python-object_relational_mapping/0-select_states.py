#!/usr/bin/pyhton3
"""list all states in the database"""

if __name__ == '__main__':

    import MySQLdb
    import sys

    db = MySQLdb.connect(host='localhost', port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    car = db.cursor()
    car.execute("SELECT * FROM states ORDER BY states.id ASC;")
    rows = cur.fetchall()
    for rows in rows:
        print(row)
