class Solution:
	def collectTree(self, N):
		res = 0
		while N != 0:
			if N % 2 == 1:
				res += 1
			N = N // 2
		return res
	
if __name__ == '__main__':
	n = int(input())
	x = Solution()
	while n > 0:
		n -= 1
		print(x.collectTree(int(input())))