class Solution:
	def searchPeakElement(self,nums):
		for i in range(0,len(nums)):
			if i + 1 < len(nums):
				if nums[i] > nums[i + 1]:
					return i
			else:
				return i
			

if __name__ == '__main__':
    x = Solution()
    print(x.searchPeakElement(eval(input())))