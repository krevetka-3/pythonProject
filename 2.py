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
    cursor.execute(students_sql)
    cursor.execute(courses_sql)
    cursor.execute(student_courses_sql)
    sqlite_connection.commit()
    age_sql = cursor.execute("""
                    SELECT * FROM students WHERE age > 30""").fetchall()
    print(age_sql)
    courses_python_sql = cursor.execute("""
                                        SELECT students.name FROM student_courses
                                        JOIN students ON students.id = student_courses.students_id
                                        JOIN courses ON courses.id = student_courses.courses_id
                                        WHERE courses.name = 'python' """).fetchall()
    print(courses_python_sql)
    courses_python_spb_sql = cursor.execute("""
                                        SELECT students.name FROM student_courses
                                        JOIN students ON students.id = student_courses.students_id
                                        JOIN courses ON courses.id = student_courses.courses_id
                                        WHERE courses.name = 'python' AND students.city = 'Spb' """).fetchall()
    print(courses_python_spb_sql)

    print("Таблица SQLite заполнена")
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")
