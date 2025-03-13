import sqlite3

con = sqlite3.connect('db2.sqlite')
cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS original_titles(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS video_products(
    id INTEGER PRIMARY KEY,
    title TEXT NOT NULL,
    original_title_id INTEGER NOT NULL UNIQUE,
    FOREIGN KEY(original_title_id) REFERENCES original_titles(id)
);
''')

original_titles = [
    (1, 'Last Action Hero'),
    (2, 'Murder, She Wrote'),
    (3, 'Looney Tunes'),
    (4, 'Il Buono, il brutto, il cattivo'),
    (5, 'Who Framed Roger Rabbit'),
    (6, 'Merrie Melodies'),
    (7, 'Mrs. \'Arris Goes to Paris')
]

video_products = [
    (1, 'Безумные мелодии Луни Тюнз', 3),
    (2, 'Весёлые мелодии', 6),
    (3, 'Кто подставил кролика Роджера', 5),
    (4, 'Хороший, плохой, злой', 4),
    (5, 'Последний киногерой', 1),
    (6, 'Она написала убийство', 2),
    (7, 'Миссис Харрис едет в Париж', 7)
]

# cur.executemany('INSERT INTO original_titles VALUES(?, ?);', original_titles)
# cur.executemany('INSERT INTO video_products VALUES(?, ?, ?);', video_products)

results = cur.execute('''
-- Вернуть поле title из таблицы video_products и поле title из original_titles
SELECT video_products.title AS translation,
       original_titles.title AS original
-- ...из двух таблиц
FROM video_products,
     original_titles
-- Выводить только те значения полей, для которых верно условие
WHERE video_products.original_title_id = original_titles.id
    AND original LIKE 'M%'
''')

for result in results:
    print(result)


con.commit()
con.close()