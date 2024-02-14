import sqlite3


def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT l.name AS lecturer_name, l.last_name AS lecturer_last_name, st.name AS student_name, 
st.last_name AS student_last_name, round(AVG(sm.mark), 2) AS avg_mark
FROM stud_marks sm
JOIN subjects s ON sm.subj_id = s.id
JOIN lecturers l ON s.lecturer_id = l.id
JOIN students st ON sm.student_id = st.id
GROUP BY l.id, st.id
ORDER BY lecturer_name, student_name;
"""

print(execute_query(sql))
