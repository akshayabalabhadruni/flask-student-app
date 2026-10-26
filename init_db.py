import sqlite3

connection = sqlite3.connect('students.db')
cursor = connection.cursor()

# Create the students table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        grade TEXT NOT NULL,
        major TEXT NOT NULL
    )
''')

# Insert sample student data
students_data = [
    ('Alice Smith', 'Sophomore', 'Computer Science'),
    ('Bob Jones', 'Junior', 'Mathematics'),
    ('Charlie Brown', 'Freshman', 'Physics')
]

cursor.executemany("INSERT INTO students (name, grade, major) VALUES (?, ?, ?)", students_data)

connection.commit()
connection.close()

print("Student database initialized successfully.")