class Solution:
	def searchInsert(self, nums: [int], target: int) -> int:
		start, end = 0, len(nums)
		while start < end:
			middle = (start + end) // 2
			if nums[middle] == target:
				return middle
			elif nums[middle] < target:
				start = middle + 1
			else:
				end = middle
			
		return start
	
if __name__ == '__main__':
    x = Solution()
    print(x.searchInsert(eval(input()),int(input())))