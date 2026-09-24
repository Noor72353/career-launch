def longest_consecutive(nums):
    """Return the length of the longest consecutive sequence."""
    numbers = set(nums)

    longest = 0

    for number in numbers:
        if number - 1 not in numbers:
            current = number
            length = 1

            while current + 1 in numbers:
                current += 1
                length += 1

            longest = max(longest, length)

    return longest
