from three_sum import three_sum


def test_three_sum_basic():
    nums = [-1, 0, 1, 2, -1, -4]

    result = three_sum(nums)

    assert sorted(result) == sorted(
        [
            [-1, -1, 2],
            [-1, 0, 1],
        ]
    )


def test_three_sum_no_solution():
    assert three_sum([1, 2, 3]) == []


def test_three_sum_empty_list():
    assert three_sum([]) == []


def test_three_sum_with_duplicates():
    assert three_sum([0, 0, 0, 0]) == [[0, 0, 0]]
