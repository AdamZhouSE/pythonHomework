class Solution:
	
	def merge(self,nums,start,middle,end):
		n1 = middle - start
		n2 = end - middle
		left = nums[start: middle]
		right = nums[middle: end]
		i = j = 0
		for k in range(start,end):
			if j >= n2 or (i < n1 and left[i] < right[j]):
				nums[k] = left[i]
				i += 1
			else:
				nums[k] = right[j]
				j += 1
	
	def mergesortAndCount(self,nums,start,end):
		if start < end - 1:
			middle = (end - start)//2 + start
			count = self.mergesortAndCount(nums, start,middle) + self.mergesortAndCount(nums,middle,end)
			j = middle
			for i in range(start, middle):
				while j < end and nums[i]/2 > nums[j]:
					j += 1
				count += (j - middle)
			self.merge(nums,start,middle,end)
			return count
		else:
			return 0
		
	
	def reversePairs(self,nums):
		return self.mergesortAndCount(nums,0,len(nums))
	
	
if __name__ == '__main__':
	nums = eval(input())
	x = Solution()
	print(x.reversePairs(nums))