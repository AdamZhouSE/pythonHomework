class Solution:
	def mergeArr(self, nums1, nums2):
		point1, point2 = len(nums1)-1, 0
		
		# 把大数都移到数组2，小数移到数组1
		while point1 >= 0 and point2 < len(nums2):
			if nums2[point2] >= nums1[point1]:
				break
			else:
				temp = nums1[point1]
				nums1[point1] = nums2[point2]
				nums2[point2] = temp
				point1 -= 1
				point2 += 1
				
		nums1.sort()
		nums2.sort()
		for num in nums1:
			print(num, end=" ")
		for i,num in enumerate(nums2):
			print(num, end=" ")
		print()
				

if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		input()
		nums1 = input().split()
		nums2 = input().split()
		x.mergeArr([int(i) for i in nums1],[int(i) for i in nums2])