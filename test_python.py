from math import pi, pow, hypot, sqrt


def test_pi():
    assert pi == 3.141592653589793


def test_pow():
    assert pow(2, 0) == 1
    assert pow(2, 3 == 8)


def test_hypot():
    assert hypot(1, 1) == 1.4142135623730951


def test_sqrt():
    assert sqrt(9) == 3


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# returns True if number is even

numbers = [1, 2, 3, 4, ]


def test_map():
    m_result = list(map(lambda x: x % 2 == 0, numbers))
    print('!!!!!!!!!!!!!!!!!!!!!', m_result)
    assert m_result == [False, True, False, True]
def test_filter():
    assert list(filter(lambda x: x % 2 == 0, numbers)) == [2, 4]
    assert list(filter(lambda x: x % 2 == 0, numbers)) == [2, 4]

    def test_map():
        m_result = list(map(lambda x: x % 2 == 0, numbers))
        print('!!!!!!!!!!!!!!!!!!!!!', m_result)
        assert m_result == [False, True, False, True]
def test_sorted():
    assert sorted(numbers) == [1, 2, 3, 4, ]

