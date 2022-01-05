numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# returns True if number is even

even_numbers_iterator = filter(lambda x:x%2==0, numbers)


def test_filter():
    assert filter(lambda x:x%2==0, numbers)== (2,4,8,10)
