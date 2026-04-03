class Solution(object):
    def capitalizeTitle(self, title):
        words = title.split()
        
        result = []
        for w in words:
            if len(w) <= 2:
                result.append(w.lower())
            else:
                result.append(w.capitalize())
        
        return " ".join(result)
