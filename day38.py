class Solution:
    def isGood(self, nums):
        n = max(nums)

        # Length must be n + 1
        if len(nums) != n + 1:
            return False

        # Expected array
        expected = list(range(1, n + 1))
        expected.append(n)

        # Compare after sorting
        return sorted(nums) == expected
