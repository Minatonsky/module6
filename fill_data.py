import random
import faker
import sqlite3

num_students = 50
num_lecturers = 5
num_groups = 3
num_subjects = 7
num_stud_marks = 20 * num_students
subjects_name = ['Computer Science', 'Physics', 'History', 'Mathematics', 'Chemistry', 'Biology', 'Literature']

fake = faker.Faker()

conn = sqlite3.connect('university.db')
cursor = conn.cursor()


def insert_fake_students(num_students):
    for _ in range(num_students):
        name = fake.first_name()
        last_name = fake.last_name()
        group_id = random.randint(1, num_groups)
        cursor.execute("INSERT INTO students (name, last_name, group_id) VALUES (?, ?, ?)", (name, last_name, group_id))


def insert_fake_lecturers(num_lecturers):
    for _ in range(num_lecturers):
        name = fake.first_name()
        last_name = fake.last_name()
        cursor.execute("INSERT INTO lecturers (name, last_name) VALUES (?, ?)", (name, last_name))


def insert_fake_subjects(num_subjects):
    for i in range(num_subjects):
        name = subjects_name[i % len(subjects_name)]
        lecturer_id = random.randint(1, num_lecturers)
        cursor.execute("INSERT INTO subjects (name, lecturer_id) VALUES (?, ?)", (name, lecturer_id))


def insert_fake_stud_marks(num_stud_marks):
    for _ in range(num_stud_marks):
        student_id = random.randint(1, num_students)
        subj_id = random.randint(1, num_subjects)
        mark = random.randint(1, 100)
        exam_date = fake.date_time_between(start_date='-150d', end_date='now')
        cursor.execute("INSERT INTO stud_marks (student_id, subj_id, mark, EXAM_DATE) VALUES (?, ?, ?, ?)",
                       (student_id, subj_id, mark, exam_date))


def insert_fake_groups(num_groups):
    for i in range(num_groups):
        group_name = f"Group-{i + 1}"
        cursor.execute("INSERT INTO groups (group_name) VALUES (?)", (group_name,))


insert_fake_lecturers(num_lecturers)
insert_fake_groups(num_groups)

insert_fake_subjects(num_subjects)
insert_fake_students(num_students)
insert_fake_stud_marks(num_stud_marks)


conn.commit()
conn.close()

