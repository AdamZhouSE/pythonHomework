class Solution:
	def reverseNum(self,nums):
		res = 0
		for i in range(len(nums)):
			for j in range(i+1, len(nums)):
				if nums[i] > nums[j]:
					res += 1
		return res


if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		input()
		nums = input().split()
		print(x.reverseNum([int(x) for x in nums]))