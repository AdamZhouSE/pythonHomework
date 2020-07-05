class Solution:
	def maxArea(self, nums):
		maxA = 0

		for i in range(len(nums)):
			count = 1
			cur = i
			while cur-1 >= 0 and nums[cur-1] > nums[i]:
				count += 1
				cur -= 1
			cur = i
			while cur + 1 < len(nums) and nums[cur+1] >= nums[i]:
				count += 1
				cur += 1
				
			maxA = max(maxA, count*nums[i])
		
		return maxA
	
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		input()
		nums = [int(i) for i in input().split()]
		print(x.maxArea(nums))