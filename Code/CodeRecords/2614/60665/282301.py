class Solution:
	def count(self, nums1, nums2, nums3):
		table = set(nums3)
		
		res = 0
		for i, j in zip(nums1, nums2):
			if (i - j) in table:
				res += 1
				
		return res
	
if __name__ == '__main__':
	n = int(input())
	x = Solution()
	while n > 0:
		n -= 1
		input()
		A = [int(i) for i in input().split()]
		B = [int(i) for i in input().split()]
		C = [int(i) for i in input().split()]
		print(x.count(A, B, C))