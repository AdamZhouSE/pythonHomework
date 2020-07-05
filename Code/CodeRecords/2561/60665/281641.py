class Solution:
	def sumCount(self, nums1, nums2, x):
		table = set()
		res = 0
		for line in nums1:
			for num in line:
				table.add(x-num)
		
		for line in nums2:
			for num in line:
				if num in table:
					res += 1
					
		return res
	

if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		info = input().split()
		N = int(info[0])
		X = int(info[1])
		nums1 = []
		for i in range(N):
			nums1.append([int(i) for i in input().split()])
		nums2 = []
		for i in range(N):
			nums2.append(([int(i) for i in  input().split()]))
		print(x.sumCount(nums1, nums2, X))