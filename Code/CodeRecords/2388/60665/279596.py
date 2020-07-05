class Solution:
	def equal(self, nums1, nums2):
		table = {}
		for num in nums1:
			if num in table:
				table[num] += 1
			else:
				table[num] = 1
				
		for num in nums2:
			if num not in table:
				return 0
			else:
				table[num] -= 1
				if table[num] < 0:
					return 0
		return 1
	
	
if __name__ == '__main__':
	n = int(input())
	x = Solution()
	while n > 0:
		n -= 1
		input()
		nums1 = input().split()
		nums2 = input().split()
		print(x.equal(nums1, nums2))