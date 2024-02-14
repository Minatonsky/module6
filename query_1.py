import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT s.id, s.name, s.last_name, round(avg(sm.mark), 2) as avg_mark 
FROM students s 
LEFT JOIN stud_marks sm ON sm.student_id = s.id
GROUP BY sm.student_id
ORDER BY avg_mark DESC
LIMIT 5;
"""

print(execute_query(sql))
