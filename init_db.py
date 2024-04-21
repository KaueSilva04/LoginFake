import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO login (usuario, senha) VALUES (?, ?)",
            ('teste', '123')
            )

connection.commit()
connection.close()