class Solution:
	def Xor(self, nums):
		for i in range(len(nums) - 1):
			nums[i] ^= nums[i + 1]
		return nums
	
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		input()
		nums = input().split()
		nums = x.Xor([int(i) for i in nums])
		for i in range(len(nums)):
			print(nums[i], end="")
			if i != len(nums) - 1:
				print(end=" ")
			else:
				print()