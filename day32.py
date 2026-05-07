class Solution(object):
    def maxValue(self, nums):
        n = len(nums)
        ans = [0] * n

        # [value, index]
        prevMax = [None] * n

        prev = (float('-inf'), -1)

        for i in range(n):
            if nums[i] > prev[0]:
                prev = (nums[i], i)

            prevMax[i] = prev

        def process(r, rightMin, rightMax):
            pMax, pivotIndex = prevMax[r]

            if pMax <= rightMin:
                currMax = pMax
            else:
                currMax = rightMax

            nextRightMin = min(pMax, rightMin)

            for i in range(pivotIndex, r + 1):
                ans[i] = currMax
                nextRightMin = min(nextRightMin, nums[i])

            if pivotIndex == 0:
                return

            process(pivotIndex - 1, nextRightMin, currMax)

        process(n - 1, float('inf'), 0)

        return ans
