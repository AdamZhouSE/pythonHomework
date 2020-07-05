class Solution:
	def trailingZeroes(self,num):
		res = 0
		num = num // 5
		while num != 0:
			res = res + num
			num = num // 5
		
		return res
	
if __name__ == '__main__':
	x = Solution()
	print(x.trailingZeroes(int(input())))