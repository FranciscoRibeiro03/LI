import sqlite3 as sql
import sys

def main(argv):
    nome = input("Nome para procurar: ")
    db = sql.connect(argv[1])

    result = db.execute("SELECT * FROM contacts WHERE firstname LIKE ? OR middlename LIKE ? OR lastname LIKE ? ORDER BY firstname ASC", (nome, nome, nome))
    count = 0
    for row in result:
        count += 1
        print(row[0])
    print(count, "contactos")

    db.close()

main(sys.argv)