class Solution:
	def search(self, nums):
		needed = -1
		maxL = max(nums[0], nums[1])
		for i in range(1,len(nums)-1):
			if nums[i] <= nums[i + 1]:
				if needed == -1 and nums[i] >= maxL:
					needed = nums[i]
				maxL = max(nums[i + 1], maxL)
			else:
				if nums[i + 1] < needed:
					needed = -1
				
		return needed
	
	
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		input()
		nums = input().split()
		print(x.search([int(i) for i in nums]))