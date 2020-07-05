class Solution:
	def subset(self, nums, x):
		if len(nums) == 0:
			return -1
		left = right = 0
		diff = -x
		
		length = len(nums)
		while right < length:
			diff += nums[right]
			
			while diff > 0:
				diff -= nums[left]
				left += 1
				
			if diff == 0:
				break
			else:
				right += 1
					
		if not diff:
			print("{:d} {:d}".format(left + 1, right + 1))
		else:
			print(-1)
			
			
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		sum = int(input().split()[1])
		nums = input().split()
		x.subset([int(i) for i in nums], sum)