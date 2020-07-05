class Solution:
	def sort(self, nums):
		left, right = 0, len(nums) - 1
		while left < right and nums[left] == 0:
			left += 1
			
		while left < right and nums[right] == 2:
			right -= 1
		
		i = left
		while i <= right:
			if nums[i] == 0:
				nums[i] = nums[left]
				nums[left] = 0
				if i == left:
					i += 1
			elif nums[i] == 2:
				nums[i] = nums[right]
				nums[right] = 2
				if i == right:
					i += 1
			else:
				i += 1
			while left < i and nums[left] == 0:
				left += 1
			while i < right and nums[right] == 2:
				right -= 1
		
		return nums
	
	
if __name__ == '__main__':
	n = int(input())
	x = Solution()
	while n > 0:
		n -= 1
		input()
		nums = input().split()
		nums = x.sort([int(i) for i in nums])
		for i in range(len(nums)):
			print(nums[i], end="")
			if i != len(nums) - 1:
				print(end=" ")
			else:
				print()