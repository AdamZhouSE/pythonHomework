class Solution:
	def countDigitOne(self, n: int) -> int:
		if n < 0:
			return 0
		
		remine = 0
		lastRound = 0
		res = 0
		extra = 1
		
		while n != 0:
			m = n % 10
			n = n // 10
			if m > 1:
				res = res + m*lastRound + extra
			elif m == 1:
				res = res + lastRound + remine + 1

			lastRound = lastRound * 10 + extra
			remine = m * extra + remine
			extra = extra * 10
		
		return res
	
if __name__ == '__main__':
	x = Solution()
	print(x.countDigitOne(int(input())))