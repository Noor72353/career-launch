from utils import is_even, square, reverse_string


def test_is_even():
    assert is_even(4) is True
    assert is_even(5) is False


def test_is_even_edge_cases():
    assert is_even(0) is True
    assert is_even(-4) is True
    assert is_even(-3) is False


def test_square():
    assert square(5) == 25
    assert square(3) == 9


def test_square_edge_cases():
    assert square(0) == 0
    assert square(-4) == 16


def test_reverse_string():
    assert reverse_string("hello") == "olleh"
    assert reverse_string("Python") == "nohtyP"


def test_reverse_string_edge_cases():
    assert reverse_string("") == ""
    assert reverse_string("a") == "a"
    assert reverse_string("  hello  ") == "  olleh  "
