import sys
import unittest


class TestExample(unittest.TestCase):
    """Демонстрирует возможности по пропуску тестов."""

    # Тест не будет запущен.
    @unittest.skip('Этот тест мы просто пропускаем')
    def test_show_msg(self):
        self.assertTrue(False, 'Значение должно быть истинным')

    # Тест будет запущен, если версия питона отлична от 3.9.
    @unittest.skipIf(sys.version_info.major == 3 and sys.version_info.minor == 9,
                     'Пропускаем, если питон 3.9')
    def test_python3_9(self):        
        # В декораторе skipIf можно проверять версии библиотек, 
        # доступность внешних сервисов,
        # время или дату - любые данные.
        pass

    # Тест будет запущен только в Linux.
    @unittest.skipUnless(sys.platform.startswith('linux'), 'Тест только для Linux')
    def test_linux_support(self):        
        pass

    # Ожидаем, что этот тест будет провален.
    @unittest.expectedFailure
    def test_fail(self):
        self.assertTrue(False, 'Ожидаем истинное значение')