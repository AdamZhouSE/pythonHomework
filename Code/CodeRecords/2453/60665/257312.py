class Solution:
	def binarySearch(self, nums, start, end, target):
		if start > end:
			return False
		if start == end:
			if nums[start] != target:
				return False
		
		middle = (start + end) // 2
		if target == nums[start]:
			return True
		if target == nums[end]:
			return True
		while middle < end:
			if target == nums[middle]:
				return True
			if nums[middle] > nums[start]:
				if target > nums[middle]:
					return self.binarySearch(nums, middle + 1, end, target)
				else:
					if target < nums[start]:
						return self.binarySearch(nums, middle + 1, end, target)
					else:
						return self.binarySearch(nums, start, middle - 1, target)
			elif nums[middle] < nums[start]:
				if target < nums[middle]:
					return self.binarySearch(nums, start, middle - 1, target)
				else:
					if target > nums[end]:
							return self.binarySearch(nums, start, middle - 1, target)
					else:
						return self.binarySearch(nums, middle + 1, end, target)
			else:
				middle = middle + 1
		return self.binarySearch(nums,start,(start + end)//2-1,target)
	
	def search(self, nums: [int], target: int) -> int:
		return self.binarySearch(nums, 0, len(nums) - 1, target)


if __name__ == '__main__':
	x = Solution()
	nums = eval(input())
	target = int(input())
	print(x.search(nums, target))