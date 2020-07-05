class Solution:
	def searchOdd(self, nums):
		table = set()
		for num in nums:
			if num in table:
				table.discard(num)
			else:
				table.add(num)
		
		return table.pop()
	
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		input()
		nums = input().split()
		print(x.searchOdd([int(i) for i in nums]))