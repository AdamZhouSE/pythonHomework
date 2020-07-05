class Solution:
	def subUnion(self, nums1, nums2):
		nums1 = set(nums1)
		
		flag = True
		for num in nums2:
			if num not in nums1:
				flag = False
				break
		
		if flag:
			print("Yes")
		else:
			print("No")
			

if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		input()
		nums1 = input().split()
		nums2 = input().split()
		x.subUnion([int(i) for i in nums1], [int(i) for i in nums2])