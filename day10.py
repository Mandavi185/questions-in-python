class Solution(object):
    def sumOfLargestPrimes(self, s):

        def isPrime(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        primes = set()
        n = len(s)

        for i in range(n):
            for j in range(i, n):
                num = int(s[i:j+1])
                if isPrime(num):
                    primes.add(num)

        primes = sorted(primes, reverse=True)
        return sum(primes[:3])                        
      
