class Solution:
	def theif(self, nums):
		if len(nums) == 0:
			return 0
		elif len(nums) <= 2:
			return max(nums)
		maxV = 0
		beforeV = 0
		for num in nums:
			num += maxV
			maxV = max(maxV, beforeV)
			beforeV = num
		
		return max(maxV, beforeV)
	
	
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		input()
		nums = input().split()
		print(x.theif([int(i) for i in nums]))