class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        banned_set = set(banned)
        
        for c in "!?',;.":
            paragraph = paragraph.replace(c, " ")
        
        words = paragraph.lower().split()
        
        count = {}
        max_word = ""
        max_count = 0
        
        for word in words:
            if word not in banned_set:
                count[word] = count.get(word, 0) + 1
                if count[word] > max_count:
                    max_count = count[word]
                    max_word = word
        
        return max_word
