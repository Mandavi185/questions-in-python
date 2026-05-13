class Solution:
    def minMoves(self, nums, limit):
        n = len(nums)

        # difference array
        diff = [0] * (2 * limit + 2)

        for i in range(n // 2):
            a = nums[i]
            b = nums[n - 1 - i]

            x = min(a, b)
            y = max(a, b)

            # Initially all sums need 2 moves

            # For sums in [x+1, y+limit]
            # moves become 1
            diff[x + 1] -= 1
            diff[y + limit + 1] += 1

            # For sum = a+b
            # moves become 0
            diff[a + b] -= 1
            diff[a + b + 1] += 1

        pairs = n // 2

        # Initially every pair needs 2 moves
        current = 2 * pairs
        ans = float('inf')

        for s in range(2, 2 * limit + 1):
            current += diff[s]
            ans = min(ans, current)

        return ans
