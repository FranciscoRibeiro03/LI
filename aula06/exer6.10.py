import sqlite3 as sql
import sys

def main(argv):
    db = sql.connect(argv[1])
    db.close()

main(sys.argv)