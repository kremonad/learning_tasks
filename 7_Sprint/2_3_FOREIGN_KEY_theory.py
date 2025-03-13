import sqlite3

con = sqlite3.connect('db.sqlite')

cur = con.cursor()

cur.executescript('''
CREATE TABLE IF NOT EXISTS wrapper(
id INTEGER PRIMARY KEY,
title TEXT
);

CREATE TABLE IF NOT EXISTS ice_cream(
id INTEGER PRIMARY KEY,
title TEXT,
description TEXT,
wrapper_id INTEGER UNIQUE,
FOREIGN KEY(wrapper_id) REFERENCES wrapper(id)
);
''')

results = cur.execute('''
SELECT ice_cream.title, wrappers.title AS wrapper
FROM ice_cream, wrappers
WHERE ice_cream.wrapper_id = wrappers.id AND wrapper LIKE 'Б%';
''')

for result in results:
    print(result)

con.close()