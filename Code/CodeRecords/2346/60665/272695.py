class Solution:
	def spiralMartix(self, nums, m, n):
		x = y = 0
		left = upper = 0
		right, lower = n - 1, m - 1
		state = 1
		res = []
		
		while left <= right and upper <= lower:
			res.append(nums[y * n + x])
			if state == 1:
				x += 1
				if x == right:
					upper += 1
					state = 2
			elif state == 2:
				y += 1
				if y == lower:
					right -= 1
					state = 3
			elif state == 3:
				x -= 1
				if x == left:
					lower -= 1
					state = 4
			elif state == 4:
				y -= 1
				if y == upper:
					left += 1
					state = 1
		res.append(nums[y * n + x])
		return " ".join(res)
	
	
if __name__ == '__main__':
	x = Solution()
	num = int(input())
	while num > 0:
		num -= 1
		mAndN = input().split()
		m = int(mAndN[0])
		n = int(mAndN[1])
		nums = input().split()
		print(x.spiralMartix(nums,m,n),end=" ")
		print()