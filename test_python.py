import math
from decimal import Decimal as dcm


M_TEST_TUPLE = (15, -33, 8, -43, 42)
M_TEST_SET = {'str1', 'str2', 'str55', 'str14', 'str09'}
M_TEST_LIST = [14, -9, 88, -12, -37, 46, dcm('-0.001'), dcm('0.001')]


def remove_negatives(x):
    """
    Отфильтровывает отрицательные числа. если объект - строка, то он попадает в итог
    :param x: объект для проверки
    :return: 1 - включать объект в результат
             0 - исключать объект из результата
    """
    if isinstance(x, str):
        return 1
    else:
        if int(x) >= 0:
            return 1
    return 0


def add_two(x):
    """
    Добавляет 2 для числовых типов или _two в конец строки
    :param x: объект для проверки
    :return: новое значение
    """
    if isinstance(x, str):
        return f'{x}_two'
    return x + 2


def test_filter():
    for elem in list(filter(remove_negatives, M_TEST_TUPLE)):
        assert 1 == remove_negatives(elem)

    for elem in list(filter(remove_negatives, M_TEST_SET)):
        assert 1 == remove_negatives(elem)

    for elem in list(filter(remove_negatives, M_TEST_LIST)):
        assert 1 == remove_negatives(elem)


def test_map():
    for elem in list(map(add_two, M_TEST_TUPLE)):
        if isinstance(elem, str):
            assert add_two(elem) == f'{elem}_two'
        else:
            assert add_two(elem) == elem + 2

    for elem in list(map(add_two, M_TEST_SET)):
        if isinstance(elem, str):
            assert add_two(elem) == f'{elem}_two'
        else:
            assert add_two(elem) == elem + 2

    for elem in list(map(add_two, M_TEST_LIST)):
        if isinstance(elem, str):
            assert add_two(elem) == f'{elem}_two'
        else:
            assert add_two(elem) == elem + 2


def test_sorted():
    """
    проверяем прямые сортировки, т.е по возрастанию.
    чтобы не рисовать совю сортировку, для проверки сделаем следующие допущения:
        - количество элементов осталось неизменным
        - первый элемент является минимальным
        - последний элемент является максимальным
    если все три проверки ок - значит отсортировалось корректно.
    """
    m_obj = sorted(M_TEST_LIST)
    m_min = min(M_TEST_LIST)
    m_max = max(M_TEST_LIST)
    m_len = len(M_TEST_LIST)
    assert len(m_obj) == m_len
    assert m_min == m_obj[0]
    assert m_max == m_obj[-1]

    m_obj = sorted(M_TEST_SET)
    m_min = min(M_TEST_SET)
    m_max = max(M_TEST_SET)
    m_len = len(M_TEST_SET)
    assert len(m_obj) == m_len
    assert m_min == m_obj[0]
    assert m_max == m_obj[-1]

    m_obj = sorted(M_TEST_TUPLE)
    m_min = min(M_TEST_TUPLE)
    m_max = max(M_TEST_TUPLE)
    m_len = len(M_TEST_TUPLE)
    assert len(m_obj) == m_len
    assert m_min == m_obj[0]
    assert m_max == m_obj[-1]


def test_pi():
    # посчитаем через ряд Лейбница и сравним 5 знаков после запятой
    m_pi = dcm('0.0')
    m_sign = 1
    for i in range(1, 265000, 2):  # только при таком количестве итераций, вышли на совпадение после 5го знака
        m_pi += m_sign * dcm('4.0') / dcm(str(i))
        m_sign *= -1
    assert round(m_pi, 5) == round(dcm(math.pi), 5)


def test_sqrt():
    for i in range(1, 20):
        assert math.sqrt(i*i) == i


def test_pow():
    for x in range(1, 100, 3):
        for y in range(-2, 3):
            assert math.pow(x, y) == x ** y


def test_hypot():
    for x in range(-5, 6):
        for y in range(-5, 6):
            assert round(math.hypot(x, y), 8) == round(math.sqrt(x * x + y * y), 8)
            # hypot вернул 15 знаков после запятой, а sqrt - 16... пришлось округлять 
