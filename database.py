import sqlite3

DATABASE = "students.db"


def get_connection():
    return sqlite3.connect(DATABASE)


def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            marks1 INTEGER NOT NULL,
            marks2 INTEGER NOT NULL,
            marks3 INTEGER NOT NULL,
            total INTEGER NOT NULL,
            grade TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


def add_student(name, marks1, marks2, marks3, total, grade):
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        INSERT INTO students
        (name, marks1, marks2, marks3, total, grade)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        name,
        marks1,
        marks2,
        marks3,
        total,
        grade
    ))

    connection.commit()
    connection.close()


def get_students():
    connection = get_connection()
    cursor = connection.cursor()

    cursor.execute("""
        SELECT
            id,
            name,
            marks1,
            marks2,
            marks3,
            total,
            grade
        FROM students
    """)

    students = cursor.fetchall()

    connection.close()

    return students