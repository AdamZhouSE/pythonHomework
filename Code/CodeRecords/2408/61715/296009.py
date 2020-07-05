import math
class Solution :
    def isPrime(self, n):
        for i in range(2, int(math.sqrt(n)) + 1) :
            if n % i == 0 :
                return False
        return True
    def primeArrange(self):
        n = int(input())
        primeNum = 0
        PrimeNum = 1
        CompositeNum = 1
        for i in range(2, n +1) :
            if Solution.isPrime(self, i) :
                primeNum += 1
        compositeNum = n - primeNum
        for i in range(2, primeNum+1) :
            PrimeNum *= i
        for i in range(2, compositeNum+1) :
            CompositeNum *= i
        print(PrimeNum*CompositeNum)
solution = Solution()
solution.primeArrange()