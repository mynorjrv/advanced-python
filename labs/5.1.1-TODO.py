from contextlib import closing
import sqlite3

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
                connection.commit()

    def find_task(self, task_name:str) -> tuple|None:
        with closing( sqlite3.connect(self.__db_name) ) as connection:
            with connection:
                c = connection.cursor()
                c.execute(
                    '''SELECT *
                    FROM tasks
                    WHERE ?
                    );''',
                    (task_name)
                )
                task = c.fetchone()
        return task
    
    def add_task(self):
        name = input('Enter task name: ')
        priority = int(input('Enter priority: '))

        name = self.__check_name(name)
        priority  = self.__check_priority(priority)
        
        with closing( sqlite3.connect(self.__db_name) ) as connection:
            with connection:
                c = connection.cursor()
                c.execute(
                    'INSERT INTO tasks (name, priority) VALUES (?,?)', 
                    (name, priority)
                )
                connection.commit()

    def print_all_tasks(self) -> None:
        with closing( sqlite3.connect(self.__db_name) ) as connection:
            with connection:
                c = connection.cursor()
                for row in c.execute('SELECT * FROM tasks'):
                    print(row)

    def __check_name(self, name:str) -> str:
        if name == '':
            raise ValueError(
                'Task name cannot be empty.'
            )
        if not self.find_task(name):
            raise Exception(
                'Task name reapeted'
            )
        return name
    
    def __check_priority(self, priority:int) -> int:
        if priority < 0:
            raise ValueError(
                'Priority cannot be less than 1.'
            )
        return priority