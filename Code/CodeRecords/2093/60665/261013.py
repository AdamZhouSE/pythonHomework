class Solution:
	def permuation(self,n,k):
		nums = set()
		res = [""]*n
		k = k-1
		N = 1
		for i in range(1,n+1):
			nums.add(i)
			N = N * i
		for i in range(0,n):
			N = N // len(nums)
			index = 0
			if N == 0:
				index = 0
			else:
				index = k//N
				k = k % N
			res[i] = str(list(nums)[index])
			nums.discard(int(res[i]))
		
		return "".join(res)
	
if __name__ == '__main__':
	x = Solution()
	print(x.permuation(int(input()),int(input())))