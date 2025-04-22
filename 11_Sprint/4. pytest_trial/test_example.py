# test_example.py
import pytest
from time import sleep

def one_more(x):
    return x + 1


@pytest.mark.parametrize(
    'input_arg, expected_result',  # Названия аргументов, передаваемых в тест.
    [
        (4, 5),
        pytest.param(3, 5, marks=pytest.mark.xfail)  # Ожидается падение теста
    ],  # Список кортежей со значениями аргументов.
    ids=['First parameter', 'Second parameter',] # Можно дать им осмысленные имена
)
def test_one_more(input_arg, expected_result):  # Те же параметры, что и в декораторе.
    assert one_more(input_arg) == expected_result


@pytest.mark.skip(reason='Что-то не работает')  # Маркер.
def test_fail():
    print('Неправильный тест')  # Новая строка.
    assert one_more(3) == 5


def get_sort_list(string):
    new_list = sorted(string.split(', '))  # Сортируем список.
    return new_list 


def test_sort():
    """Тестируем функцию get_sort_list()."""
    result = get_sort_list('Яша, Саша, Маша, Даша')
    assert result == ['Даша', 'Маша', 'Саша', 'Яша']


@pytest.mark.slowww  # Отмечаем маркером тест.
def test_type():
    """Тестируем тип данных, возвращаемых из get_sort_list()."""
    sleep(3)  # Трёхсекундная пауза.
    result = get_sort_list('Яша, Саша, Маша, Даша')
    # Провальный тест:
    # ожидаем число, но вернётся список.
    assert isinstance(result, int)


def cartesian_product(a, b):
    return a * b


@pytest.mark.parametrize('x', [1, 2])
@pytest.mark.parametrize('y', ['one', 'two'])
def test_cartesian_product(x, y):
    assert cartesian_product(x, y) is not None