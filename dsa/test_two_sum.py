from two_sum import Solution


def test_two_sum_basic():
    solution = Solution()

    assert solution.twoSum([2, 7, 11, 15], 9) == [0, 1]


def test_two_sum_middle_elements():
    solution = Solution()

    assert solution.twoSum([3, 2, 4], 6) == [1, 2]


def test_two_sum_duplicate_values():
    solution = Solution()

    assert solution.twoSum([3, 3], 6) == [0, 1]


def test_two_sum_negative_numbers():
    solution = Solution()

    assert solution.twoSum([-3, 4, 2, -1], 1) == [0, 1]
