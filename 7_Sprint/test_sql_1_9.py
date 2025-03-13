import sqlite3
'''Напишите запрос, который сосчитает суммарную стоимость
 опубликованных на главной странице сортов мороженого — тех, 
 у каких одновременно есть статусы «опубликовано» и «показать на главной». 
 Результат выведите в консоль.
'''

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

# Напишите SQL запрос в строке.
results = cur.execute('''
SELECT SUM(price)
FROM ice_cream
WHERE is_published = TRUE AND is_on_main = TRUE;
''')


for result in results:
    print(result)

con.close()