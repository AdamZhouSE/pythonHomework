class Solution:
	def waveArr(self, nums):
		for i in range(1,len(nums),2):
			temp = nums[i]
			nums[i] = nums[i - 1]
			nums[i - 1] = temp
	
if __name__ == '__main__':
	n = int(input())
	x = Solution()
	while n > 0:
		n -= 1
		input()
		nums = input().split()
		x.waveArr(nums)
		for i in range(len(nums)):
			print(nums[i], end="")
			if i != len(nums) - 1:
				print(end=" ")
			else:
				print()