class Solution:
	def countNumbersWithUniqueDigits(self, n: int) -> int:
		if n == 0:
			return 1
		res, muls = 10, 9
		for i in range(1, min(n, 10)):
			muls *= 10 - i
			res += muls
		return res
	
if __name__ == '__main__':
	x = Solution()
	print(x.countNumbersWithUniqueDigits(int(input())))