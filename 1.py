import sqlite3

try:
    sqlite_connection = sqlite3.connect('sqlite_python.db')
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
                                        id INTEGER PRIMARY KEY,
                                        students_id INTEGER,
                                        courses_id INTEGER, 
                                        FOREIGN KEY(students_id) REFERENCES students (id),
                                        FOREIGN KEY(courses_id) REFERENCES courses (id)
                                        );'''
    cursor = sqlite_connection.cursor()
    print("База данных подключена к SQLite")
    cursor.execute(sqlite_create_table_students)
    cursor.execute(sqlite_create_table_courses)
    cursor.execute(sqlite_create_table_student_courses)

    sqlite_connection.commit()
    print("Таблица SQLite создана")

    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
