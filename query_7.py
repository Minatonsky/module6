import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT s.name, s.last_name, sbj.name, sm.mark, sm.EXAM_DATE 
FROM students s
LEFT JOIN groups g ON g.id = s.group_id
LEFT JOIN stud_marks sm ON sm.student_id = s.id
LEFT JOIN subjects sbj ON sbj.id = sm.subj_id
WHERE g.group_name = 'Group-2' AND sbj.name = 'Computer Science';
"""

print(execute_query(sql))
