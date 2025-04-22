import unittest


class Calculator:
    """Производит арифметические действия."""

    def summ(self, *args):
        """
        Возвращает сумму принятых аргументов,
        если аргументов нет, возвращает None.
        """
        if len(args) == 0:
            return None
        return sum(args)


class TestCalc(unittest.TestCase):
    """Тестируем Calculator."""

    @classmethod
    def setUpClass(cls):
        """Вызывается один раз перед запуском всех тестов класса."""
        cls.calc = Calculator()

    def test_summ_no_arguments(self):
        """Тестируем summ() без аргументов."""
        with self.subTest("Должен вернуть None при отсутствии аргументов"):
            result = self.calc.summ()
            self.assertIsNone(result)

    def test_summ_with_arguments(self):
        """Тестируем summ() с различными аргументами."""
        test_cases = [
            ("Один аргумент", (5,), 5),
            ("Несколько аргументов", (2, 3), 5),
            ("Много аргументов", (1, 2, 3, 4, 5), 15),
            ("Отрицательные числа", (-1, -2, 3), 0),
            ("Дробные числа", (1.5, 2.5), 4.0),
            ("Смешанные типы чисел", (1, 2.5, -3), 0.5),
            ("Нули", (0, 0, 0), 0),
        ]

        for desc, args, expected in test_cases:
            with self.subTest(desc):
                result = self.calc.summ(*args)
                self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
