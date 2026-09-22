class Solution:
    def containsDuplicate(self, nums):
        return len(nums) != len(set(nums))


solution = Solution()

print(solution.containsDuplicate([1, 2, 3, 1]))
print(solution.containsDuplicate([1, 2, 3, 4]))
print(solution.containsDuplicate([1, 1]))
