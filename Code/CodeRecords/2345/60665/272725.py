class Solution:
	def numberCheck(self, nums, n):
		number = set(i + 1 for i in range(n))
		repeat = []
		for num in nums:
			if num not in number:
				repeat.append(num)
			else:
				number.discard(num)
		if not number:
			return 0, 0
		return min(repeat), min(number)
	
if __name__ == '__main__':
	x = Solution()
	num = int(input())
	while num > 0:
		num -= 1
		n = int(input())
		nums = input().split()
		res = x.numberCheck([int(x) for x in nums], n)
		print(res[0],end=" ")
		print(res[1])