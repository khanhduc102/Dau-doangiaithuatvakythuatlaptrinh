class Solution(object):
    def targetIndices(self, nums, target):
        less = 0
        equal = 0
        
        for num in nums:
            if num < target:
                less += 1
            elif num == target:
                equal += 1
        
        return [less + i for i in range(equal)]
