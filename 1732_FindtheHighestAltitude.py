class Solution(object):
    def largestAltitude(self, gain):
        current = 0
        max_alt = 0
        
        for g in gain:
            current += g
            max_alt = max(max_alt, current)
        
        return max_alt
