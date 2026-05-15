import heapq
import math

class Solution(object):
    def pickGifts(self, gifts, k):
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)
        
        for _ in range(k):
            largest_pile = -heapq.heappop(max_heap)
            gifts_left = int(math.sqrt(largest_pile))

            heapq.heappush(max_heap, -gifts_left)
            
        return -sum(max_heap)