import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT sbj.name, s.name AS student_name, s.last_name AS student_last_name, l.name AS lecturer_name, l.last_name AS lecturer_last_name 
FROM students s
JOIN stud_marks sm ON sm.student_id = s.id
JOIN subjects sbj ON sbj.id = sm.subj_id
JOIN lecturers l ON l.id = sbj.lecturer_id
GROUP BY s.id, sbj.id
ORDER BY s.name, s.last_name;
"""

print(execute_query(sql))
