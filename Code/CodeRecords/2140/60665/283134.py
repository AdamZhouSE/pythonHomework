class Solution:
	def roll(self, n):
		res = [n]
		
		for i in range(n - 1, 0, -1):
			index = i % (n - i + 1)
			res = res[n-i-index:n-i] + [i] + res[0:n-i-index]
		
		return res
	
if __name__ == '__main__':
	n = int(input())
	x = Solution()
	while n > 0:
		n -= 1
		N = int(input())
		res = x.roll(N)
		for i in range(len(res)):
			print(res[i],end="")
			if i != len(res) - 1:
				print(end=" ")
			else:
				print()