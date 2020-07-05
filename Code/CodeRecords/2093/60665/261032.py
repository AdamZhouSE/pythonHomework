class Solution:
	def getPermutation(self,n,k):
		nums = [""]*n
		res = [""]*n
		k = k-1
		N = 1
		for i in range(1,n+1):
			nums[i-1] = str(i)
			N = N * i
		for i in range(0,n):
			N = N // len(nums)
			index = 0
			if N == 0:
				index = 0
			else:
				index = k//N
				k = k % N
			res[i] = nums[index]
			del nums[index]
		
		return "".join(res)
	
if __name__ == '__main__':
	x = Solution()
	print(x.getPermutation(int(input()),int(input())))