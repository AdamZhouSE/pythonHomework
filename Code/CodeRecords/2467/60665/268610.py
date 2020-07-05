class Solution:
	def findKth(self,nums1,nums2,k):
		length1 = len(nums1)
		length2 = len(nums2)
		num = [nums1,nums2]
		if length1 == 0 and length2 == 0:
			return
		if length1 == 0:
			choose = 1
			another = 2**31
		elif length2 == 0:
			choose = 0
			another = 2**31
		else:
			if nums1[0] > nums2[0]:
				choose = 0
				another = nums2[0]
			else:
				choose = 1
				another = nums1[0]
		
		res = 0
		point = [0, 0]
		for i in range(0,k):
			if num[choose][point[choose]] <= another:
				res = num[choose][point[choose]]
				point[choose] += 1
			else:
				res = another
				another = num[choose][point[choose]]
				choose = 1 - choose
				point[choose] += 1
		return res
	
	
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
	    n -= 1
	    k = int(input().split()[2])
	    nums1 = input().split()
	    nums2 = input().split()
	    print(x.findKth([int(x) for x in nums1],[int(x) for x in nums2],k))
				