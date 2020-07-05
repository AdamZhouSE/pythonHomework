class Solution:
	def judegSum(self,nums,sum):
		diff = set()
		for num in nums:
			if num in diff:
				return "Yes"
			if num <= sum:
				diff.add(sum - num)
		return "No"
	
	
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		sum = int(input().split()[1])
		nums = input().split()
		print(x.judegSum([int(i) for i in nums],sum))