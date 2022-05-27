import sqlite3 as sql
import sys

def main(argv):
    db = sql.connect(argv[1])

    result = db.execute("SELECT firstname FROM contacts ORDER BY firstname ASC")
    count = 0
    for row in result:
        count += 1
        print(row[0])
    print(count, "contactos")

    db.close()

main(sys.argv)