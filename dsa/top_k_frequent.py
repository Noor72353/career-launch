from collections import Counter


def top_k_frequent(nums, k):
    """Return the k most frequent elements."""
    frequency = Counter(nums)

    most_common = frequency.most_common(k)

    return [item[0] for item in most_common]


nums = [1, 1, 1, 2, 2, 3]
k = 2

result = top_k_frequent(nums, k)

print(result)
