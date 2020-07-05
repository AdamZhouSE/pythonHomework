class Solution:
	def partReverse(self, nums, k):
		for i in range(0, len(nums), k):
			start = i
			end = min(start +  k, len(nums))
			while start < end:
				temp = nums[start]
				nums[start] = nums[end - 1]
				nums[end - 1] = temp
				start += 1
				end -= 1
		return nums
	
	
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		k = int(input().split()[1])
		nums = input().split()
		x.partReverse(nums, k)
		print(" ".join(nums), end=" ")
		print()

		