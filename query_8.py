import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT l.name, l.last_name, s.name AS subject_name, round(avg(sm.mark), 2) AS average_mark
FROM lecturers l
JOIN subjects s ON s.lecturer_id = l.id
JOIN stud_marks sm ON sm.subj_id = s.id
GROUP BY l.id, s.id;
"""

print(execute_query(sql))
