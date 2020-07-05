class Solution:
	def findLengthOfLCIS(self, nums: [int]) -> int:
		if len(nums) == 0:
			return 0
		lonLength = length = 1
		pre = nums[0]
		for num in nums:
			if num > pre:
				length = length + 1
			else:
				if length > lonLength:
					lonLength = length
				length = 1
			pre = num
		if length > lonLength:
			lonLength = length
		return lonLength
		
if __name__ == '__main__':
    x = Solution()
    print(x.findLengthOfLCIS(eval(input())))