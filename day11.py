class Solution(object):
    def minimumAverage(self, nums):
        nums.sort()

        i = 0
        j = len(nums) - 1
        min_avg = float('inf')

        while i < j:
            avg = (nums[i] + nums[j]) / 2.0

            min_avg = min(min_avg, avg)

            i += 1
            j -= 1

        return min_avg
        
