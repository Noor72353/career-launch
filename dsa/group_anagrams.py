def group_anagrams(words):
    """Group words that are anagrams of each other."""
    groups = {}

    for word in words:
        key = "".join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]

result = group_anagrams(words)

print(result)
