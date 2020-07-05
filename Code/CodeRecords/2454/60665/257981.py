class Solution:
	def findMin(self, nums):
		start, end = 0, len(nums) - 1
		
		while start < end:
			if nums[start] < nums[end]:
				break
			middle = (start + end) // 2
			while middle <= end:
				if nums[middle] > nums[start]:
					start = middle + 1
					break
				elif nums[middle] < nums[start]:
					end = middle
					break
				else:
					if nums[start] == nums[end]:
						middle = middle + 1
						continue
					else:
						start = middle + 1
						break
			if middle > end:
				end = (start + end) // 2
		
		return nums[start]
	

if __name__ == '__main__':
    x = Solution()
    print(x.findMin(eval(input())))
