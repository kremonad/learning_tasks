digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6, 6, 11, 10]

# Массив с другим набором ключей: это цвета карт.
card_colors = [
    'Аметистовый',   # [0]
    'Чёрный',        # [1]
    'Белый',         # [2]
    'Жёлтый',        # [3] 
    'Синий',         # [4]
    'Фиолетовый',    # [5]
    'Коричневый',    # [6]
    'Зелёный',       # [7]
    'Розовый',       # [8]
    'Серо-голубой',  # [9]
    'Бобровый',      # [10]
    'Коралловый',    # [11]
    'Ванильный'      # [12]
]


def card_strength(idx):
    # Получаем количество букв для числа idx.
    return digit_lengths[idx]


# Добавляем функцию, передающую значения ключей из массива card_colors:
def card_background(idx):
    # Получаем название цвета для карты idx.
    return card_colors[idx]


def insertion_sort_by_key(arr, key):
    for i in range(1, len(arr)):
        current = arr[i]
        prev = i - 1
        while prev >= 0 and key(arr[prev]) > key(current):
            arr[prev + 1] = arr[prev]
            prev -= 1
        arr[prev + 1] = current


cards = [2, 9, 11, 7, 1]
# Сортируем по длине слов:
insertion_sort_by_key(cards, card_strength)
# Печатаем результат:
print('По длине слов:', cards)

# Вызываем ту же функцию, но сортируем по названиям цветов:
insertion_sort_by_key(cards, card_background)
# Печатаем результат:
print('По цветам:', cards)

#######################

digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6, 6, 11, 10]


def card_strength(idx):
    return digit_lengths[idx]


cards = [2, 9, 11, 7, 1]
# В параметр key передаём функцию, возвращающую значения ключей.
result = sorted(cards, key=card_strength)
print(result)

#######################

digit_lengths = [4, 4, 3, 3, 6, 4, 5, 4, 6, 6, 6, 11, 10]
cards = [2, 9, 11, 7, 1]
# В параметр key передаём лямбда-функцию, возвращающую значения ключей.
result = sorted(cards, key=lambda x: digit_lengths[x])
print(result)