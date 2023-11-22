import sqlite3

try:
    """
    Создание Базы данных sqlite_python.db
    """
    sqlite_connection = sqlite3.connect('sqlite_python.db')
    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")

    class Create:
        def init(self):
            """
            Созадние таблиц
            """
            sqlite_create_table_students = '''CREATE TABLE IF NOT EXISTS students (
                                            id INTEGER PRIMARY KEY,
                                            name TEXT NOT NULL,
                                            surname TEXT NOT NULL,
                                            age INTEGER NOT NULL,
                                            city TEXT NOT NULL);'''
            sqlite_create_table_courses = """CREATE TABLE IF NOT EXISTS  courses (
                                            id INTEGER PRIMARY KEY,
                                            name TEXT NOT NULL,
                                            time_start TEXT NOT NULL,
                                            time_end TEXT NOT NULL); """

            sqlite_create_table_student_courses = '''CREATE TABLE IF NOT EXISTS student_courses (
                                                    students_id INTEGER,
                                                    courses_id INTEGER,
                                                    FOREIGN KEY(students_id) REFERENCES students (id),
                                                    FOREIGN KEY(courses_id) REFERENCES courses (id)
                                                    );'''
            try:
                cursor.execute(sqlite_create_table_students)
                cursor.execute(sqlite_create_table_courses)
                cursor.execute(sqlite_create_table_student_courses)
            except:
                print('не выполнено!')
            finally:
                sqlite_connection.commit()
                print("Таблица SQLite создана")

    class Insert:
        def init(self):
            """
            Заполнение таблиц
            """
            students_sql = """
                            INSERT INTO students(id,name,surname,age,city) VALUES
                            (1, 'Max', 'Brooks', 24, 'Spb'),
                            (2, 'John', 'Stones', 15, 'Spb'),
                            (3, 'Andy', 'Wings', 45, 'Manchester'),
                            (4, 'Kate', 'Brooks', 34, 'Spb')"""
            courses_sql = """
                            INSERT INTO courses(id,name,time_start,time_end) VALUES
                            (1, 'python', '21.07.21', '21.08.21'),
                            (2, 'java', '13.07.21', '16.08.21')"""
            student_courses_sql = """
                                    INSERT INTO student_courses(students_id,courses_id) VALUES
                                    (1, 1),
                                    (2, 1),
                                    (3, 1),
                                    (4, 2)"""
            try:
                cursor.execute(students_sql)
                cursor.execute(courses_sql)
                cursor.execute(student_courses_sql)
            except:
                print('не выполнено!')
            finally:
                sqlite_connection.commit()


    class Select:
        def init(self):
            """
            Выполнение выборки
            """
            a = cursor.execute("""
                            SELECT * FROM students WHERE age > 30""").fetchall()

            b = cursor.execute("""
                            SELECT students.name FROM student_courses
                            JOIN students ON students.id = student_courses.students_id
                            JOIN courses ON courses.id = student_courses.courses_id
                            WHERE courses.name = 'python' """).fetchall()

            c = cursor.execute("""
                                    SELECT students.name FROM student_courses
                                    JOIN students ON students.id = student_courses.students_id
                                    JOIN courses ON courses.id = student_courses.courses_id
                                    WHERE courses.name = 'python' AND students.city = 'Spb' """).fetchall()
finally:
                sqlite_connection.commit()

class SQLInput:
        """
        Класс содержащий функции быстрого произвольного запроса
        """
        @staticmethod
        def execute_sql(text_sql):
            """
            Функция быстрого выполнение запроса
            :param text_sql: type is str. команда sql
            :return: type is str. результат выборки
            """
            a = cursor.execute(text_sql).fetchall()
            print(a)

        @staticmethod
        def execute_sql_console():
            """
            Функция ввода с консоли
            :return: type is str. результат выборки
            """
            text_sql = input()
            a = cursor.execute(text_sql).fetchall()
            print(a)


Create()
Insert()
Select()

SQLInput.execute_sql_console()

cursor.close()
except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
