from longest_consecutive import longest_consecutive


def test_longest_consecutive():
    assert longest_consecutive([100, 4, 200, 1, 3, 2]) == 4


def test_longest_consecutive_with_duplicates():
    assert longest_consecutive([1, 2, 2, 3]) == 3
