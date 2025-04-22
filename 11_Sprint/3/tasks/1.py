import unittest


class Calculator:
    """Производит арифметические действия."""

    def divider(self, num1, num2):
        """Возвращает результат деления num1 / num2."""
        if num2 == 0:
            raise ZeroDivisionError('Не могу делить на ноль')
        return num1 / num2


class TestCalc(unittest.TestCase):
    """Тестируем Calculator."""

    # Подготовьте данные для теста при помощи фикстур.
    @classmethod
    def setUpClass(cls):
        cls.calc = Calculator() 

    def test_divider(self):
        act = TestCalc.calc.divider(4,2)  # вызовите метод divider с валидными аргументами.
        self.assertEqual(act, 2, 'Ошибка в методе divider()')

    def test_divider_zero_division(self):
        # Проверьте, что деление на 0 выбрасывает исключение
        with self.assertRaises(ZeroDivisionError,
                               msg='Ожидалась ошибка деления на ноль'):
            self.calc.divider(4,0)