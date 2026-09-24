from container_with_most_water import max_area


def test_max_area_basic():
    assert max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49


def test_max_area_two_lines():
    assert max_area([1, 1]) == 1


def test_max_area_decreasing_heights():
    assert max_area([5, 4, 3, 2, 1]) == 6


def test_max_area_empty_list():
    assert max_area([]) == 0
