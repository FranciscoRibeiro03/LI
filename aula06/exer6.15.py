import sqlite3 as sql

def main():
    db = sql.connect("Chinook_Sqlite.sqlite")

    result = db.execute("SELECT Customer.FirstName,Customer.LastName FROM Invoice,Customer WHERE Customer.CustomerId = Invoice.CustomerId")
    dic = {}
    for row in result:
        name = row[0] + " " + row[1]
        dic[name] = dic.get(name, 0) + 1
    
    for name, count in sorted(dic.items(), key=lambda x: x[1], reverse=True)[:10]:
        print("{} - {}".format(name, count))

    db.close()

main()