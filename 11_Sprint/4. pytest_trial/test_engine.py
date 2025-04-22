# test_engine.py
import pytest

# Импортируем класс двигателя.
from engine_class import Engine

@pytest.fixture(scope='session')
def engine():
    """Фикстура возвращает экземпляр класса двигателя."""
    print('Engine factory')  # Добавьте вывод сообщения.
    return Engine()


# Эта фикстура не возвращает никаких значений, но изменяет объект,
# созданный другой фикстурой.
@pytest.fixture
def start_engine(engine):  # Вызываем фикстуру получения объекта двигателя.
    """Фикстура запускает двигатель."""
    # Изменяем значение свойства объекта:
    engine.is_running = True


def test_engine_is_running(engine, start_engine):  # Вызываем обе фикстуры.
    """Тест проверяет, работает ли двигатель."""
    assert engine.is_running  # Проверяем, что значение атрибута is_running это True.

###--------------------------------------------------------------------------###
# Добавляем маркер и указываем название фикстуры строкой.
@pytest.mark.usefixtures('start_engine') 
def test_engine_is_running(engine):  # А из параметров функции фикстуру start_engine убираем.
    assert engine.is_running 

###--------------------------------------------------------------------------###
@pytest.fixture(autouse=True)  # Обозначаем фикстуру как автоматически вызываемую.
def start_engine(engine):
    """Фикстура запускает двигатель."""
    engine.is_running = True


# Вызываем только одну фикстуру. 
# Запуск двигателя выполнится автоматически, без вызова.
def test_engine_is_running(engine):  
    """Тест проверяет, работает ли двигатель."""
    assert engine.is_running 


# Допишите новый тест.
def test_check_engine_class(engine):
    """Тест проверяет класс объекта."""
    assert isinstance(engine, Engine) 


@pytest.fixture(autouse=True)
def start_engine(engine):
    """Фикстура запускает двигатель."""
    engine.is_running = True  # Запустим двигатель.
    # Распечатаем строчку до выполнения теста.
    print(f'Before test engine.is_running {engine.is_running}') 
    yield  # В этот момент начинает выполняться тест.
    engine.is_running = False  # Заглушим двигатель.
    # Распечатаем строчку после выполнения теста и остановки двигателя.
    print(f'After test engine.is_running {engine.is_running}') 


def test_engine_is_running(engine):  
    """Тест проверяет, работает ли двигатель."""
    print('test_engine_is_running')  # Выведем название теста.
    assert engine.is_running


def test_check_engine_class(engine):
    """Тест проверяет класс объекта."""
    print('test_check_engine_class')  # Выведем название теста.
    assert isinstance(engine, Engine) 