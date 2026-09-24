from top_k_frequent import top_k_frequent


def test_top_k_frequent():
    nums = [1, 1, 1, 2, 2, 3]

    assert top_k_frequent(nums, 2) == [1, 2]


def test_top_k_frequent_one():
    nums = [1, 1, 2, 3]

    assert top_k_frequent(nums, 1) == [1]


def test_top_k_frequent_all_elements():
    nums = [1, 2, 2, 3, 3, 3]

    assert top_k_frequent(nums, 3) == [3, 2, 1]


def test_top_k_frequent_empty_list():
    assert top_k_frequent([], 2) == []
