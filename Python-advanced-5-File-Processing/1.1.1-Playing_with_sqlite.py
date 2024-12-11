from contextlib import closing
import sqlite3

conn = sqlite3.connect(
    './Python-advanced-5-File-Processing/hello.db'
)

# Creates DB in RAM
#conn = sqlite3.connect(':memory:')

c = conn.cursor()
c.execute(
    '''CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        priority INTEGER NOT NULL
    );'''
)

# Inserting data
# Inserting with specific id
# INSERT INTO tasks (id, name, priority) VALUES (1, 'My first task', 1);
# Inserting with autoincrement
# INSERT INTO tasks (name, priority) VALUES ('My first task', 1);
# Insetring without specifying columns
# INSERT INTO table_name VALUES (value1, value2, value3, ..., valueN);

# ? is actually a security measure to prevent sql injection
c.execute(
    'INSERT INTO tasks (name, priority) VALUES (?,?)',
    ('My first task', 1)
)
conn.commit()
conn.close()

# Now trying the context
with closing( sqlite3.connect(
        './Python-advanced-5-File-Processing/hello.db'
    ) ) as connection:
    with connection:
        c = connection.cursor()
        c.execute(
            'INSERT INTO tasks (name, priority) VALUES (?,?)',
            ('AAAAnother task task', 5)
        )