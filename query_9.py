import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT s.name, s.last_name, sbj.name 
FROM students s
JOIN stud_marks sm ON sm.student_id = s.id
JOIN subjects sbj ON sbj.id = sm.subj_id
WHERE s.name = 'Amanda' AND  s.last_name = 'Welch'
GROUP BY s.id, sbj.id;
"""

print(execute_query(sql))
