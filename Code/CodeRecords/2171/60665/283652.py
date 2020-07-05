class Solution:
	def seperate(self, nums):
		linklist = [i for i in range(1, len(nums)+2)]
		linklist[len(nums)] = -1
		
		left = 0
		middle = right = -1
		for i in range(len(nums)):
			if nums[i] % 2 == 0:
				linklist[left] = i + 1
				left = linklist[left]
			else:
				if middle == -1:
					middle = i + 1
					right = i + 1
				else:
					linklist[right] = i + 1
					right = linklist[right]
		linklist[left] = middle
		linklist[right] = -1
		
		point = linklist[0]
		res = []
		while point != -1:
			res.append(nums[point-1])
			point = linklist[point]
		return res
		
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		input()
		nums = [int(i) for i in input().split()]
		res = x.seperate(nums)
		for i in range(len(res)):
			print(res[i], end=" ")
		print()