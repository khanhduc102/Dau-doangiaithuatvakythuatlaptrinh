class Solution(object):
    def countWords(self, words1, words2):
        from collections import Counter
        
        count1 = Counter(words1)
        count2 = Counter(words2)
        
        result = 0
        
        for word in count1:
            if count1[word] == 1 and count2[word] == 1:
                result += 1
                
        return result
