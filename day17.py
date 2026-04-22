class Solution(object):
    def secondHighest(self, s):
        digits = set()

        for ch in s:
            if ch.isdigit():
                digits.add(int(ch))

        if len(digits) < 2:
            return -1

        digits = sorted(digits, reverse = True)
        return digits[1]            
        
