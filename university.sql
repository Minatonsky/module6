-- Table: students
DROP TABLE IF EXISTS students;
CREATE TABLE students (
     id INTEGER PRIMARY KEY AUTOINCREMENT,
     name varchar(50) NOT NULL,
     last_name varchar(50) NOT NULL,
     group_id varchar(50) NOT NULL,
     FOREIGN KEY (group_id) REFERENCES groups (id)
    );

-- Table: lecturers
DROP TABLE IF EXISTS lecturers;
CREATE TABLE lecturers (
     id integer PRIMARY KEY AUTOINCREMENT,
     name varchar(50) NOT NULL,
     last_name varchar(50) NOT NULL
    );

-- Table: subjects
DROP TABLE IF EXISTS subjects;
CREATE TABLE subjects (
     id integer PRIMARY KEY AUTOINCREMENT,
     name varchar(50) NOT NULL,
     lecturer_id integer NOT NULL,
     FOREIGN KEY (lecturer_id) REFERENCES lecturers (id)
);

-- Table: stud_marks
DROP TABLE IF EXISTS stud_marks;
CREATE TABLE stud_marks (
     id integer PRIMARY KEY AUTOINCREMENT,
     student_id int,
     subj_id int,
     mark mark SMALLINT,
     EXAM_DATE datetime
);

-- Table: groups
DROP TABLE IF EXISTS groups;
CREATE TABLE groups (
     id integer PRIMARY KEY AUTOINCREMENT,
     group_name varchar(50) UNIQUE NOT NULL
);