# INNER JOIN (JOIN)
'''
SELECT video_products.title,
       slogans.slogan_text,
       product_types.title
FROM video_products
JOIN slogans ON video_products.slogan_id = slogans.id
JOIN product_types ON video_products.type_id = product_types.id;
'''

# LEFT OUTER JOIN (LEFT JOIN)
'''
SELECT video_products.title,
       slogans.slogan_text
FROM video_products
LEFT JOIN slogans ON video_products.slogan_id = slogans.id; 
'''

# RIGHT OUTER JOIN (RIGHT JOIN)
# выводятся все записи из правой таблицы, а к ним добавляются только те данные из левой таблицы, в которых есть ключ объединения
'''
SELECT video_products.title,
       product_types.title
FROM video_products
RIGHT JOIN product_types ON video_products.type_id = product_types.id;
'''

# FULL OUTER JOIN (FULL JOIN) выводятся все записи из объединяемых таблиц
'''
SELECT video_products.title,
       slogans.slogan_text
FROM video_products
FULL JOIN slogans ON video_products.slogan_id = slogans.id;
'''
# ==
'''SELECT video_products.title,
       slogans.slogan_text
FROM video_products
LEFT JOIN slogans ON video_products.slogan_id = slogans.id
UNION
SELECT video_products.title,
       slogans.slogan_text
FROM slogans
LEFT JOIN video_products ON video_products.slogan_id = slogans.id;'''

# CROSS JOIN (каждая запись левой таблицы объединится с каждой записью правой.)
'''SELECT video_products.title,
       slogans.slogan_text
FROM video_products
CROSS JOIN slogans;'''

('Безумные мелодии Луни Тюнз', "For Three Men The Civil War Wasn't Hell. It Was Practice!")
('Безумные мелодии Луни Тюнз', "This isn't the movies anymore")
('Безумные мелодии Луни Тюнз', 'Tonight on Murder She Wrote')
('Безумные мелодии Луни Тюнз', "I'll be back")
('Весёлые мелодии', "For Three Men The Civil War Wasn't Hell. It Was Practice!")
('Весёлые мелодии', "This isn't the movies anymore")
('Весёлые мелодии', 'Tonight on Murder She Wrote')
('Весёлые мелодии', "I'll be back")
('Хороший, плохой, злой', "For Three Men The Civil War Wasn't Hell. It Was Practice!")
('Хороший, плохой, злой', "This isn't the movies anymore")
('Хороший, плохой, злой', 'Tonight on Murder She Wrote')
('Хороший, плохой, злой', "I'll be back")
('Последний киногерой', "For Three Men The Civil War Wasn't Hell. It Was Practice!")
('Последний киногерой', "This isn't the movies anymore")
('Последний киногерой', 'Tonight on Murder She Wrote')
('Последний киногерой', "I'll be back")
('Она написала убийство', "For Three Men The Civil War Wasn't Hell. It Was Practice!")
('Она написала убийство', "This isn't the movies anymore")
('Она написала убийство', 'Tonight on Murder She Wrote')
('Она написала убийство', "I'll be back")