class Solution(object):
    def completePrime(self, num):
        
        def isprime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        s = str(num)
        n = len(s)

        for i in range(1, n + 1):
            if not isprime(int(s[:i])):
                return False

        for i in range(n):
            if not isprime(int(s[i:])):
                return False        

        return True                    
