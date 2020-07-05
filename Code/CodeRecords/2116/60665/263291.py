class Solution:
	def nthSuperUglyNumber(self, n: int, primes: [int]) -> int:
		nums = [1,]
		numOfP = len(primes)
		point = [0]*numOfP
		
		for i in range(0, n):
			ugly = 2**31
			for j in range(0,numOfP):
				ugly = min(ugly,nums[point[j]]*primes[j])
			nums.append(ugly)
			for j in range(0,numOfP):
				if ugly == nums[point[j]]*primes[j]:
					point[j] = point[j] + 1
					
		return nums[n-1]
	
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	primes = eval(input())
	print(x.nthSuperUglyNumber(n,primes))