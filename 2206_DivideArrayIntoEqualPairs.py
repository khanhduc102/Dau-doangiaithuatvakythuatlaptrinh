class Solution(object):
    def divideArray(self, nums):
        count = {}

        for num in nums:
            count[num] = count.get(num, 0) + 1

        for val in count.values():
            if val % 2 != 0:
                return False

        return True
