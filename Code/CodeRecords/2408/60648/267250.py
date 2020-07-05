class Solution:
    def numPrimeArrangements(self, n: int) -> int:
        # (sum(prime)) 的阶乘 乘以 (n - sum(prime)) 的阶乘
        def countPrimes(n: int) -> int:
            if n < 2:
                return 0
            prime = [1] * (n + 1)
            prime[0] = prime[1] = 0
            for i in range(2, int(n**0.5) +1):
                if prime[i] == 1:
                    prime[i*i:n + 1:i] = [0]*len(prime[i*i:n + 1:i])
            return sum(prime)
        def func(n):
            if n == 0 or n == 1:
                return 1
            else:
                return (n * func(n - 1))
        return func(countPrimes(n)) * func(n - countPrimes(n)) % (10**9 + 7)
        

if __name__=="__main__":
    s=int(input())
    x=Solution().numPrimeArrangements(s)
    print(x)