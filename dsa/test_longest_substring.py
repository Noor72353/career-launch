from longest_substring import length_of_longest_substring


def test_longest_substring_basic():
    assert length_of_longest_substring("abcabcbb") == 3


def test_longest_substring_repeated_characters():
    assert length_of_longest_substring("bbbbb") == 1


def test_longest_substring_mixed_characters():
    assert length_of_longest_substring("pwwkew") == 3


def test_longest_substring_empty_string():
    assert length_of_longest_substring("") == 0


def test_longest_substring_all_unique():
    assert length_of_longest_substring("abcdef") == 6
