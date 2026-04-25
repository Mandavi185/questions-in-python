# solution no 1
'''class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        set1, set2 = set(nums1), set(nums2)
        
        return[
            sum(num in set2 for num in nums1),
            sum(num in set1 for num in nums2)
        ]'''

# solution no 2        
class Solution(object):
    def findIntersectionValues(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)
        
        count1 = 0
        for num in nums1:
            if num in set2:
                count1 += 1
        
        count2 = 0
        for num in nums2:
            if num in set1:
                count2 += 1
        
        return [count1, count2]

        
