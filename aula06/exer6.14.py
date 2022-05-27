import sqlite3 as sql

def main():
    nome = input("Nome do álbum: ")
    db = sql.connect("Chinook_Sqlite.sqlite")

    result = db.execute("SELECT Album.Title,Track.Name FROM Album,Track WHERE (Album.Title LIKE ?) AND Album.AlbumId = Track.AlbumId ORDER BY Album.Title ASC", (nome,))
    count = 0
    song_names = []
    for row in result:
        song_names.append(row[1])
        count += 1
    print("O álbum {} tem {} músicas:".format(nome, count))
    for song in song_names:
        print("- {}".format(song))

    db.close()

main()