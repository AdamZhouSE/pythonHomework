class Solution:
	def rain(self, nums):
		count = 0
		leftEdge = (-1, -1)
		rightEdge = (-1, -1)
		for i, n in enumerate(nums):
			if leftEdge[0] == -1:
				if i + 1 == len(nums):
					break
				if n > nums[i + 1] and (i - 1 < 0 or n >= nums[i - 1]):
					leftEdge = [i, nums[i]]
			else:
                # 此处出错
				if n >= nums[i - 1] and (i + 1 == len(nums) or n > nums[i + 1]):
					if n >= leftEdge[1]:
						count += (i - leftEdge[0] - 1) * leftEdge [1]
						count += n
						leftEdge = (i, n)
						rightEdge = (-1, -1)
					else:
						if n > rightEdge[1]:
							rightEdge = (i, n)
				count -= n
					
		while rightEdge[0] != -1:
			count += (rightEdge[0] - leftEdge[0]) * rightEdge[1]
			leftEdge = rightEdge
			rightEdge = [-1, -1]
			for i in range(leftEdge[0] + 1,len(nums)):
				if nums[i] >= nums[i - 1] and (i + 1 == len(nums) or nums[i] > nums[i + 1]):
					if nums[i] > rightEdge[1]:
						rightEdge = (i, nums[i])
		if leftEdge[0] != -1: # 考虑恒增的情况
			for i in range(leftEdge[0] + 1, len(nums)):
				count += nums[i]
			
		return count
	
	
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		input()
		nums = input().split()
		if len(nums) < 3:
			print(0)
		else:
			print(x.rain([int(x) for x in nums]))