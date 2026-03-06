class Solution(object):
    def areOccurrencesEqual(self, s):
        count = {}
        
        for c in s:
            count[c] = count.get(c, 0) + 1
        
        values = list(count.values())
        
        for v in values:
            if v != values[0]:
                return False
        
        return True
