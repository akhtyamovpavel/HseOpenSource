import pytest

from triangle import find_triangle


def test_two():
    with pytest.raises(IndexError):
        assert find_triangle(*[1, 2]) == 'bad'


def test_equal():
    assert find_triangle(*[1, 1, 1]) == 'equal'


def test_bedr():
    assert find_triangle(*[2, 2, 3]) == 'bedr'


def test_not_triangle():
    assert find_triangle(*[1, 2, 4]) == 'bad'
