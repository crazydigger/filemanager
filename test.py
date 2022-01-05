numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# returns True if number is even
# returns True if number is even
numbers = [1, 2, 3, 4, ]


def test_map():
    m_result = list(map(lambda x: x % 2 == 0, numbers))
    print('!!!!!!!!!!!!!!!!!!!!!',m_result)
    assert m_result==[2,4]