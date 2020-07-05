class Solution:
	def countDiff(self, nums, k):
		table = {}
		copy = set()
		res = 0
		for num in nums:
			if num not in copy or k == 0:
				if num in table:
					res += table[num]
					table[num] = -1
				if k != 0:
					table[num - k] = table.get(num - k, 0) + 1
					table[num + k] = table.get(num + k, 0) + 1
				else:
					table[num] = table.get(num, 0) + 1
				copy.add(num)
		return res

if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		input()
		nums = [int(i) for i in input().split()]
		k = int(input())
		print(x.countDiff(nums, k))
		