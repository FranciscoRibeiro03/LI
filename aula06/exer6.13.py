import sqlite3 as sql
import sys

def main(argv):
    nome = argv[2]
    db = sql.connect(argv[1])

    result = db.execute("SELECT contacts.firstname,contacts.middlename,contacts.lastname,companies.name FROM contacts,companies WHERE (contacts.firstname LIKE ? OR contacts.middlename LIKE ? OR contacts.lastname LIKE ?) AND contacts.company_id = companies.id ORDER BY contacts.firstname ASC", (nome, nome, nome))
    count = 0
    for row in result:
        print("A pessoa {} pertence à empresa {}".format(f"{row[0]} {row[1]} {row[2]}", row[3]))

    db.close()

main(sys.argv)