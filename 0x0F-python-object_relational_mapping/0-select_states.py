#!/usr/bin/python3
"""
This script lists all the states in the database hbtn_0e_0_usa
and it takes user,password and the name of the database as arguments.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3])
    cur = db.cursor()
    cur.execute('SELECT * FROM states ORDER BY id ASC')
    results = cur.fetchall()
    for result in results:
        print(result)
