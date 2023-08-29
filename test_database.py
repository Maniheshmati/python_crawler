import sqlite3

conn = sqlite3.connect("crawler.db")
cur = conn.cursor()

# cur.execute("SELECT * FROM categories")
# rows = cur.fetchall()
# for row in rows:
#     print(row)

# cur.close()