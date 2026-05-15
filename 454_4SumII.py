class Solution(object):
    def fourSumCount(self, nums1, nums2, nums3, nums4):
        from collections import defaultdict
        
        sum_map = defaultdict(int)
        
        for a in nums1:
            for b in nums2:
                sum_map[a + b] += 1
        
        count = 0
    
        for c in nums3:
            for d in nums4:
                count += sum_map[-(c + d)]
        
        return count
