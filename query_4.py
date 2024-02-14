import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT g.group_name, round(avg(sm.mark), 2)avg_mark 
FROM groups g
JOIN students s ON s.group_id = g.id
JOIN stud_marks sm ON sm.student_id = s.id
GROUP BY g.id;
"""

print(execute_query(sql))
