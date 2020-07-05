class Solution:
	def searchNearest(self, nums, target):
		diff = 2*31 - 1
		for num in nums:
			temp = num - target
			if abs(temp) < abs(diff):
				diff = temp
			elif abs(temp) == abs(diff):
				if temp > diff:
					diff = temp
					
		return target + diff
	

if __name__ == '__main__':
	n = int(input())
	x = Solution()
	while n > 0:
		n -= 1
		target = int(input().split()[1])
		nums = input().split()
		print(x.searchNearest([int(i) for i in nums], target))