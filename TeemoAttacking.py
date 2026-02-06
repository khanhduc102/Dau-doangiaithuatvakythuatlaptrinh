class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        if not timeSeries or duration == 0:
            return 0
        
        total = 0
        
        for i in range(len(timeSeries) - 1):
            total += min(duration, timeSeries[i + 1] - timeSeries[i])
    
        total += duration
        
        return total
