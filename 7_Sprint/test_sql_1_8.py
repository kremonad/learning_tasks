import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

# Напишите SQL запрос в строке.
results = cur.execute('''
SELECT title, description
FROM ice_cream
WHERE is_published = TRUE
ORDER BY title DESC
LIMIT 2 OFFSET 1;
''')


for result in results:
    print(result)

con.close()