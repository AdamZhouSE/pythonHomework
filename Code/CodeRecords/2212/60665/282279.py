class Solution:
		def countFactor(self, primes, factors, k, res):
			if k == len(primes):
				return res
			else:
				count = 0
				for i in range(factors[primes[k]]+1):
					count += self.countFactor(primes, factors, k+1, res*primes[k]**i)
				return count
			
		def divisorsSum(self, n):
			factors = {}
			rest = n
			i = 2
			
			while i*i <= rest:
				while rest%i == 0:
					factors[i] = factors.get(i, 0) + 1
					rest = rest // i
				i += 1
			if rest > 1:
				factors[rest] = factors.get(rest, 0) + 1
			
			primes = list(factors.keys())
			return self.countFactor(primes, factors, 0, 1)
		
if __name__ == '__main__':
	T = int(input())
	x = Solution()
	while T > 0:
		T -= 1
		n = int(input())
		if x.divisorsSum(n) < n*2:
			print(1)
		else:
			print(0)