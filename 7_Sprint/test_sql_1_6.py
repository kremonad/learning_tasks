import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

# Запрашиваем все столбцы всех записей из таблицы video_products;
# символ * после SELECT означает "верни все поля найденных записей".
results = cur.execute('''
  SELECT *
  FROM video_products;
''')

# В results получим итерируемый объект, который можно перебрать циклом:
for result in results:
    print(result)

# При получении данных из таблицы не нужно вызывать метод con.commit()!
con.close()