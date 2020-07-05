class Solution:
	def numSquares(self,num):
		res = [x for x in range(0,num+1)]
		for i in range(4,num+1):
			for j in range(0,int(i**(0.5))+1):
				res[i] = min(res[i], res[i - j*j] + 1)
		return res[num]
		
		
if __name__ == '__main__':
	x = Solution()
	print(x.numSquares(int(input())))