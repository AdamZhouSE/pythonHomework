class Solution:
	def leastChange(self, s):
		table = set()
		res = 0
		for le in s:
			if le in table:
				res += 1
			else:
				table.add(le)
		return res
	
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		print(x.leastChange(input()))