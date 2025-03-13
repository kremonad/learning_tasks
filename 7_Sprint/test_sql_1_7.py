import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

# Напишите SQL запрос в строке.
cur.execute('''
SELECT tbl_name FROM sqlite_master where type='table';
''')

table = cur.fetchall()[0][0]  # Получите имя таблицы через атрибут курсора.
print(table)
# Напишите SQL запрос в строке.
results = cur.execute(f'''
SELECT title, description
FROM {table};
''')


for result in results:
    print(result)

con.close()