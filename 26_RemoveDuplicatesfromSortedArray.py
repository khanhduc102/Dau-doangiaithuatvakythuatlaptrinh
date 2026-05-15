class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        insert_pos = 1
        
        for curr in range(1, len(nums)):
            if nums[curr] != nums[curr - 1]:
                nums[insert_pos] = nums[curr]
                insert_pos += 1
                
        return insert_pos