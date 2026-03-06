class Solution(object):
    def sortPeople(self, names, heights):
        people = zip(heights, names)
        people = sorted(people, reverse=True)
        
        result = []
        for h, name in people:
            result.append(name)
        
        return result
