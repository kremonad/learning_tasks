def series_sum(incoming):
    # Конкатенирует все элементы списка, приводя их к строкам.
    result = ''
    for i in incoming:
        result += str(i)
    return result


# Первое тестирование: проверьте, корректно ли сработает функция series_sum(),
# если ей на вход передать список из целых и дробных чисел.

mixed_numbers = [0, 1, 2, 2.2, 4.1]
result_numbers = '0122.24.1'

# Вместо многоточия напишите утверждение, которое должно быть проверено.
assert series_sum(mixed_numbers) == result_numbers, (
    'Функция series_sum() некорректно обрабатывает смешанный список из int и float.'
)

# Второе тестирование: проверьте, корректно ли сработает функция series_sum(),
# если ей на вход передать список из чисел и строк.

mixed_numbers_strings = [0, 1, 2, 'abc', 'vvv']
result_numbers_strings = '012abcvvv'

# Вместо многоточия напишите утверждение, которое должно быть проверено.
assert series_sum(mixed_numbers_strings) == result_numbers_strings, (
    'Функция series_sum() некорректно обрабатывает смешанный список из чисел и строк.'
)

# Третье тестирование: проверьте, корректно ли сработает функция series_sum(),
# если ей на вход передать пустой список.
empty = []
result_empty = ''

# Вместо многоточия напишите утверждение, которое должно быть проверено.
assert series_sum(empty) == result_empty, (
    'Функция series_sum() некорректно обрабатывает пустой список'
)