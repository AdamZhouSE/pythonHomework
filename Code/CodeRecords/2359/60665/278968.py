class Solution:
	def triCount(self, nums):
		table = set(nums)
		
		res = 0
		for i in range(len(nums)):
			for j in range(i+1,len(nums)):
				if (nums[i] + nums[j]) in table:
					res += 1
					
		if res == 0:
			return -1
		else:
			return res
	
	
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		input()
		nums = input().split()
		print(x.triCount([int(i) for i in nums]))