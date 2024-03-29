import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT s.name AS student_name, s.last_name AS student_last_name, g.group_name, sbj.name AS subj_name, sm.EXAM_DATE 
FROM students s
JOIN stud_marks sm ON sm.student_id = s.id AND date(sm.EXAM_DATE) = (SELECT max(date(sm2.EXAM_DATE)) FROM stud_marks sm2 WHERE sm2.subj_id = sbj.id)
JOIN groups g ON g.id = s.group_id
JOIN subjects sbj ON sm.subj_id = sbj.id
WHERE g.group_name = 'Group-3' AND sbj.name = 'History';
"""

print(execute_query(sql))
