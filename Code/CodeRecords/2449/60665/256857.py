class Solution:
	def binarySearch(self,nums,start,end,target):
		if start > end:
			return -1
		if start == end:
			if nums[start] != target:
				return -1
		
		middle = (start + end)//2
		if target == nums[middle]:
			return middle
		if target == nums[start]:
			return start
		if target == nums[end]:
			return end
		
		if nums[middle] > nums[start]:
			if target > nums[middle]:
				return self.binarySearch(nums,middle+1,end,target)
			else:
				if target < nums[start]:
					return self.binarySearch(nums,middle+1,end,target)
				else:
					return self.binarySearch(nums,start,middle-1,target)
		elif nums[middle] < nums[start]:
			if target < nums[middle]:
				return self.binarySearch(nums,start,middle-1,target)
			else:
				if target > nums[end]:
					return self.binarySearch(nums,start,middle-1,target)
				else:
					return self.binarySearch(nums,middle+1,end,target)
		else:
			if nums[middle] == nums[end]:
				return self.binarySearch(nums,start,middle-1,target)
			else:
				return self.binarySearch(nums,middle+1,end,target)
				
			
	
	def search(self, nums: [int], target: int) -> int:
		return self.binarySearch(nums,0,len(nums)-1,target)
		
		
if __name__ == '__main__':
    x = Solution()
    nums = eval(input())
    target = int(input())
    print(x.search(nums,target))