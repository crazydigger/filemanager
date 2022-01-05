from fmanager import creator
from victory import long_date


def test_creator():
    assert creator() == 'создатель программы:Рома Боровиков(c)(r)'


def test_long_date():
    assert long_date('01') == 'января'
    assert long_date('13') == ''
