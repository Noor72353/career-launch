from dsa.utils import is_even, square, reverse_string


def test_is_even():
    assert is_even(4) is True
    assert is_even(5) is False


def test_square():
    assert square(5) == 25
    assert square(3) == 9


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"
