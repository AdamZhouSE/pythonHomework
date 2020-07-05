class Solution:
	def binary(self, n):
		for i in range(1, n+1):
			print("{0:b}".format(i),end=' ')
		print()
				
if __name__ == '__main__':
	n = int(input())
	x = Solution()
	while n > 0:
		n -= 1
		x.binary(int(input()))