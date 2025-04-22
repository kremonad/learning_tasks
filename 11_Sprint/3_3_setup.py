import unittest


def setUpModule():
    """Вызывается один раз перед запуском любого класса из файла."""
    print('> setUpModule')


def tearDownModule():
    """Вызывается один раз после запуска любого класса из файла."""
    print('> tearDownModule')


class TestExample(unittest.TestCase):
    """Демонстрирует принцип работы тестов."""

    @classmethod
    def setUpClass(cls):
        """Вызывается один раз перед запуском всех тестов класса."""
        print('>> setUpClass')

    @classmethod
    def tearDownClass(cls):
        """Вызывается один раз после запуска всех тестов класса."""
        print('>> tearDownClass')

    def setUp(self):
        """Подготовка прогона теста. Вызывается перед каждым тестом."""
        print('>>> setUp')

    def tearDown(self):
        """Вызывается после каждого теста."""
        print('>>> tearDown')

    def test_one(self):  # Это имитация обычного теста.
        print('>>>> test_one')

    def test_one_more(self): # Имитация другого теста.
        print('>>>> test_one_more')


class YetAnotherTestExample(unittest.TestCase):
    """В этом тестовом классе нет никаких фикстур."""

    def test_without_class_fixtures(self):
        print('>>>> test_without_class_fixtures')