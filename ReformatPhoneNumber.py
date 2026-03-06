class Solution(object):
    def reformatNumber(self, number):
        digits = ""
        
        for c in number:
            if c.isdigit():
                digits += c
        
        res = []
        i = 0
        n = len(digits)
        
        while n - i > 4:
            res.append(digits[i:i+3])
            i += 3
        
        if n - i == 4:
            res.append(digits[i:i+2])
            res.append(digits[i+2:i+4])
        else:
            res.append(digits[i:])
        
        return "-".join(res)
