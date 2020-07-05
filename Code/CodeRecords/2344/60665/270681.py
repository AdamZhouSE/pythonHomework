class Solution:
	def rover(self,nums, d):
		res = [x for x in nums[d:]]
		for x in nums[0:d]:
			res.append(x)
		return res
	
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		input()
		nums = input().split()
		d = int(input())
		res = x.rover(nums, d)
		print(" ".join(res),end=" ")
		print()