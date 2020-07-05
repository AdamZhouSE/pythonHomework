class Solution:
	def searchRange(self, nums: [int], target: int) -> [int]:
		start, end = 0, len(nums)
		while start < end:
			middle = (start + end)//2
			if nums[middle] == target:
				head, tail = middle - 1, middle + 1
				flagH = flagT = True
				while flagH or flagT:
					if head < start or nums[head] != target:
						flagH = False
					else:
						head = head - 1
					if tail >= end or nums[tail] != target:
						flagT = False
					else:
						tail = tail + 1
				return [head + 1, tail - 1]
			elif nums[middle] < target:
				start = middle + 1
			else:
				end = middle
		
		return [-1,-1]
				
if __name__ == '__main__':
    x = Solution();
    print(x.searchRange(eval(input()),int(input())))