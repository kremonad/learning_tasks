from unittest import TestCase


def get_square(num):
    """Возвращает квадрат полученного аргумента"""
    return num ** 2


class TestExample(TestCase):

    def test_square(self):
        """Тест возведения в квадрат."""
        # Проверим три утверждения: при возведении первого числа в квадрат
        # функция вернёт второе число.
        # Исходные данные соберём в кортеж, содержащий в себе другие кортежи.
        values_results = (
            (2, 4),   # С этими параметрами тест вернёт OK.
            (3, 10),  # С этими параметрами тест провалится.
            (4, 20),  # И с этими параметрами - тоже провалится.
        )
        # Цикл, в котором кортежи, вложенные в values_results, 
        # распаковываются в переменные value и expected_result:
        for value, expected_result in values_results:
            # subTest в качестве контекстного менеджера.
            with self.subTest(
                    f'Возведение числа {value} в квадрат дало результат,\n'
                    f'отличающийся от ожидаемого {expected_result}',
                    value=value, 
                    expected_result=expected_result,
            ):
                result = get_square(value)
                # Тестовое утверждение, которое будет вызвано несколько раз
                # с разными значениями переменных.
                self.assertEqual(result, expected_result)