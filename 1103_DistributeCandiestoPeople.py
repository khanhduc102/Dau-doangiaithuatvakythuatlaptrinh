class Solution(object):
    def distributeCandies(self, candies, num_people):
        res = [0] * num_people
        give = 1
        i = 0
        
        while candies > 0:
            person = i % num_people
            
            if candies >= give:
                res[person] += give
                candies -= give
            else:
                res[person] += candies
                break
            
            give += 1
            i += 1
        
        return res
