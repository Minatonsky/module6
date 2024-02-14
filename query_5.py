import sqlite3
#ЗАВДАННЯ. Знайти які курси читає певний викладач.
#трохи неоднозначне завдання. якщо мається на увазі що має бути умова where і по прізвищу викладача знайти який предмет викладає
#то при новій генерації бд будуть нові прізвища викладачів, тому зробив повний список по викладачам

def execute_query(sql: str) -> list:
    with sqlite3.connect('university.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


sql = """
SELECT l.name, l.last_name, s.name as subj 
FROM lecturers l
JOIN subjects s ON s.lecturer_id = l.id
ORDER BY l.name;
"""

print(execute_query(sql))
