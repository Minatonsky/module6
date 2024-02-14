import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT g.group_name, round(avg(sm.mark), 2) as avg_mark, sbj.name AS subj_name 
FROM students s 
JOIN stud_marks sm ON sm.student_id = s.id
JOIN subjects sbj ON sbj.id = sm.subj_id
JOIN groups g ON g.id = s.group_id
GROUP BY g.id, sbj.id
ORDER BY g.group_name, avg_mark desc;
"""

print(execute_query(sql))
