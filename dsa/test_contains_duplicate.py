from contains_duplicate import Solution


def test_contains_duplicate():
    solution = Solution()

    assert solution.containsDuplicate([1, 2, 3, 1]) is True


def test_contains_duplicate_false():
    solution = Solution()

    assert solution.containsDuplicate([1, 2, 3, 4]) is False


def test_contains_duplicate_same_values():
    solution = Solution()

    assert solution.containsDuplicate([1, 1]) is True


def test_contains_duplicate_empty_list():
    solution = Solution()

    assert solution.containsDuplicate([]) is False
