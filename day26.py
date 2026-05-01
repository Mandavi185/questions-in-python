class Solution:
    def maxRotateFunction(self, nums):
        n = len(nums)
        
        total_sum = sum(nums)
        
        # Compute F(0)
        F = 0
        for i in range(n):
            F += i * nums[i]
        
        max_value = F
        
        # Compute F(1) to F(n-1)
        for k in range(1, n):
            F = F + total_sum - n * nums[n - k]
            max_value = max(max_value, F)
        
        return max_value  
