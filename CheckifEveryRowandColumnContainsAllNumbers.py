class Solution(object):
    def checkValid(self, matrix):
        n = len(matrix)
        valid = set(range(1, n + 1))
        
        for row in matrix:
            if set(row) != valid:
                return False
        
        for col in range(n):
            col_set = set()
            for row in range(n):
                col_set.add(matrix[row][col])
            if col_set != valid:
                return False
        
        return True
