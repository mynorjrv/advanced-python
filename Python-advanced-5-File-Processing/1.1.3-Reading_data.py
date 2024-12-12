import sqlite3

conn = sqlite3.connect(
    'Python-advanced-5-File-Processing/hello.db'
)
c = conn.cursor()
for row in c.execute('SELECT * FROM tasks'):
    print(row)
conn.close()


# Fetching all is less efficient
conn = sqlite3.connect(
    'Python-advanced-5-File-Processing/hello.db'
)
c = conn.cursor()
c.execute('SELECT * FROM tasks')
rows = c.fetchall()
for row in rows:
    print(row)
conn.close()


# Or again, instead of iterating I can fetch
# one by one
conn = sqlite3.connect(
    'Python-advanced-5-File-Processing/hello.db'
)
c = conn.cursor()
c.execute('SELECT * FROM tasks')
row = c.fetchone()
print(row)
row = c.fetchone()
print(row)
conn.close()
