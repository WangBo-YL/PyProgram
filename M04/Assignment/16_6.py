import sqlite3

conn = sqlite3.connect('books.db')
curs = conn.cursor()
curs.execute('SELECT title FROM books ORDER BY title ASC')
titles = curs.fetchall()

for title in titles:
    print(title[0])

conn.close()