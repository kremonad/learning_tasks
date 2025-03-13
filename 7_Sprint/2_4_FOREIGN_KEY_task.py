import sqlite3

con = sqlite3.connect('db.sqlite')
cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS categories(
id INTEGER PRIMARY KEY,
slug TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS ice_cream(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT,
price REAL NOT NULL,
category_id INTEGER NOT NULL,
FOREIGN KEY(category_id) REFERENCES categories(id)
);

''')

results = cur.execute('''
SELECT ice_cream.title, categories.slug, MAX(ice_cream.price)
FROM ice_cream, categories
WHERE ice_cream.category_id = categories.id
GROUP BY categories.slug
ORDER BY ice_cream.price DESC; 
''')

for result in results:
    print(result)

con.close()