from valid_anagram import Solution


def test_valid_anagram():
    solution = Solution()

    assert solution.isAnagram("anagram", "nagaram") is True


def test_not_anagram():
    solution = Solution()

    assert solution.isAnagram("rat", "car") is False


def test_anagram_different_words():
    solution = Solution()

    assert solution.isAnagram("listen", "silent") is True


def test_different_lengths():
    solution = Solution()

    assert solution.isAnagram("hello", "hell") is False


def test_empty_strings():
    solution = Solution()

    assert solution.isAnagram("", "") is True
