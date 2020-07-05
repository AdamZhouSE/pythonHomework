class Solution:
	def sumOfSub(self, nums):
		table = set()
		left = 0
		res = 0
		
		for right in range(len(nums)):
			while nums[right] in table:
				table.discard(nums[left])
				left += 1
			
			table.add(nums[right])
			n = right - left + 1
			res += n*(n+1)//2
			
		return res
	
if __name__ == '__main__':
	x = Solution()
	T = int(input())
	while T > 0:
		T -= 1
		input()
		nums = input().split()
		print(x.sumOfSub(nums))