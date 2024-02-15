import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT l.name, l.last_name, s.name as subj 
FROM lecturers l
JOIN subjects s ON s.lecturer_id = l.id
WHERE l.name = 'Jason' AND l.last_name = 'Perez';
"""

print(execute_query(sql))
