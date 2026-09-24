def length_of_longest_substring(text):
    """Return the length of the longest substring without repeating
    characters.
    """
    seen = set()
    left = 0
    maximum = 0

    for right in range(len(text)):
        while text[right] in seen:
            seen.remove(text[left])
            left += 1

        seen.add(text[right])

        current_length = right - left + 1
        maximum = max(maximum, current_length)

    return maximum
