from contextlib import closing
import sqlite3

# Checks if table exists in DB to prevent sql injection if talbe name
# should be passed.
def exists_table(db, name):
    query = "SELECT 1 FROM sqlite_master WHERE type='table' and name = ?"
    return db.execute(query, (name,)).fetchone() is not None

class Todo:
    def __init__(self, db_name:str):
        self.__db_name = db_name
        self.__create_task_table()
        
    def __create_task_table(self):
        with closing( sqlite3.connect(self.__db_name) ) as connection:
            with connection:
                c = connection.cursor()
                c.execute(
                    '''CREATE TABLE IF NOT EXISTS tasks (
                    id INTEGER PRIMARY KEY,
                    name TEXT NOT NULL,
                    priority INTEGER NOT NULL
                    );'''
                )
                # with connection auto commits or rollback
                # connection.commit()

    def find_task(self, task_name:str) -> tuple|None:
        with closing( sqlite3.connect(self.__db_name) ) as connection:
            with connection:
                c = connection.cursor()
                c.execute(
                    '''SELECT *
                    FROM tasks
                    WHERE name=?
                    ;''',
                    # (str) es str, la tupla necesita coma
                    (task_name,)
                )
                task = c.fetchone()
        return task
    
    def add_task(self):
        name = input('Enter task name: ')
        name = self.__check_name(name)

        priority = int(input('Enter priority: '))
        priority  = self.__check_priority(priority)
        
        with closing( sqlite3.connect(self.__db_name) ) as connection:
            with connection:
                c = connection.cursor()
                c.execute(
                    'INSERT INTO tasks (name, priority) VALUES (?,?)', 
                    (name, priority)
                )
                # connection.commit()

    def print_all_tasks(self) -> None:
        with closing( sqlite3.connect(self.__db_name) ) as connection:
            with connection:
                c = connection.cursor()
                for row in c.execute('SELECT * FROM tasks'):
                    print(row)

    def change_priority(self, id:int, priority:int):
        priority = self.__check_priority(priority)
        with closing( sqlite3.connect(self.__db_name) ) as connection:
            with connection:
                c = connection.cursor()
                c.execute(
                    'UPDATE tasks SET priority = ? WHERE id = ?', 
                    (priority, id)
                )

    def delete_task(self, id:int):
        with closing( sqlite3.connect(self.__db_name) ) as connection:
            with connection:
                c = connection.cursor()
                c.execute(
                    'DELETE FROM tasks WHERE id = ?', 
                    (id,)
                )

    def __check_name(self, name:str) -> str:
        if name == '':
            raise ValueError(
                'Task name cannot be empty.'
            )
        if self.find_task(name):
            raise Exception(
                'Task name reapeted'
            )
        return name
    
    def __check_priority(self, priority:int) -> int:
        if priority < 1:
            raise ValueError(
                'Priority cannot be less than 1.'
            )
        return priority

if __name__ == '__main__':
    a = Todo('Lab.db')

    a.add_task()
    a.add_task()
    a.add_task()
    a.add_task()