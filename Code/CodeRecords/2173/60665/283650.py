class Solution:
	def count(self, n):
		res = 0
		for i in range(1, n+1):
			res += (2*i-1)*(n+1-i)
		return res
	
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		print(x.count(int(input())))