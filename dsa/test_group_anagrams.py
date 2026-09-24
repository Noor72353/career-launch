from group_anagrams import group_anagrams


def test_group_anagrams():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]

    result = group_anagrams(words)

    normalized_result = sorted([sorted(group) for group in result])
    expected = sorted(
        [
            ["eat", "tea", "ate"],
            ["tan", "nat"],
            ["bat"],
        ]
    )

    assert normalized_result == sorted([sorted(group) for group in expected])


def test_group_anagrams_empty_list():
    assert group_anagrams([]) == []


def test_group_anagrams_single_word():
    assert group_anagrams(["hello"]) == [["hello"]]


def test_group_anagrams_no_matches():
    words = ["cat", "dog", "sun"]

    result = group_anagrams(words)

    assert sorted([sorted(group) for group in result]) == [
        ["cat"],
        ["dog"],
        ["sun"],
    ]
