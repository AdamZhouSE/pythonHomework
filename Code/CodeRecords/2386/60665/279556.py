class Solution:
	def fourSum(self, nums, X):
		nums.sort()
		for i in range(len(nums)):
			for j in range(i+1,len(nums)):
				left = j + 1
				right = len(nums) - 1
				while left < right:
					sum = nums[i] + nums[j] + nums[left] + nums[right]
					if sum == X:
						return 1
					if sum < X:
						left += 1
					if sum > X:
						right -= 1
						
		return 0
	
	
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		input()
		nums = input().split()
		X = int(input())
		print(x.fourSum([int(i) for i in nums], X))