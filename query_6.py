import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT g.group_name, s.name, s.last_name 
FROM students s
LEFT JOIN groups g ON g.id = s.group_id
WHERE g.group_name = 'Group-2';
"""

print(execute_query(sql))
