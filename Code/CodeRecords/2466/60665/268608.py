class Solution:
	def numOfTri(self,nums):
		if len(nums) < 3:
			return 0
		
		nums.sort()
		res = 0
		length = len(nums)
		for i in range(0, length - 2):
			for j in range(i + 1, length - 1):
				for k in range(j + 1, length):
					if nums[i] + nums[j] > nums[k]:
						res += 1
					else: break
		return res
	
	
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		m = int(input())
		sides = input().split()
		print(x.numOfTri([int(x) for x in sides]))