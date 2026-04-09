class Solution(object):
    def greatestLetter(self, s):
        s_set = set(s)
        result = ""
        for ch in s_set:
            if ch.islower() and ch.upper() in s_set:
               result = max(result, ch.upper()) 
        return result      

       
