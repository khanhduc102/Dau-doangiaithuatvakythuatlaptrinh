class Solution(object):
    def distributeCandies(self, candyType):
        n = len(candyType)
        so_loai = len(set(candyType))
        return min(so_loai, n // 2)
