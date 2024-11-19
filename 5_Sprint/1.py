def second_element(card_and_length):
    return card_and_length[1]


cards = [
    (2, 'Белый'),
    (9, 'Серо-голубой'),
    (11, 'Коралловый'),
    (7, 'Зелёный'),
    (1, 'Чёрный')
]
result = sorted(cards, key=second_element)
print(result)
# [(2, 'Белый'), (7, 'Зелёный'), (11, 'Коралловый'), (9, 'Серо-голубой'), (1, 'Чёрный')]