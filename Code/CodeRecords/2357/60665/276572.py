class Solution:
	def find(self, nums1, nums2,x):
		for i in range(len(nums1)):
			nums1[i] = x - nums1[i]
		for num in nums1:
			if num < 0:
				continue
			for n in nums2:
				if num == n:
					print("{:d} {:d}".format(x - num, n))
					
					
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		num = int(input().split()[2])
		nums1 = input().split()
		nums2 = input().split()
		x.find([int(i) for i in nums1],[int(i) for i in nums2], num)