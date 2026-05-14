class Solution(object):
    def checkIfExist(self, arr):
        seen = set()
        
        for num in arr:
            # Check if double or half already exists
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            
            seen.add(num)
        
        return False