class Solution(object):
    def countElements(self, nums):
        min_val = min(nums)
        max_val = max(nums)
        
        count = 0
        
        for x in nums:
            if min_val < x < max_val:
                count += 1
        
        return count
