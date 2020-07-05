class Solution:
	def select(self, nums):
		minN = [0]*2
		maxN = [0]*3
		
		for num in nums:
			if num < 0:
				if num < minN[0]:
					if num < minN[1]:
						minN[0] = minN[1]
						minN[1] = num
					else:
						minN[0] = num
			if num > 0:
				if num > maxN[0]:
					if num > maxN[1]:
						if num > maxN[2]:
							maxN[0] = maxN[1]
							maxN[1] = maxN[2]
							maxN[2] = num
						else:
							maxN[0] = maxN[1]
							maxN[1] = num
					else:
						maxN[0] = num
		
		res1 = maxN[0] * maxN[1] * maxN[2]
		res2 = minN[0] * minN[1] * maxN[2]
		return max(res1, res2)
	
	
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		input()
		nums = input().split()
		print(x.select([int(i) for i in nums]))