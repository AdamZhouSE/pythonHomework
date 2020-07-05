class Solution:
	def minSubArrayLen(self, s: int, nums: [int]) -> int:
		count = length = head = tail = diff = 0
		for i in range(0, len(nums)):
			count = count + nums[i]
			if count >= s:
				if length == 0:
					head = i
					diff = count - s
					if diff > 0:
						while diff >= 0:
							diff = diff - nums[tail]
							tail = tail + 1
						tail = tail - 1
						diff = diff + nums[tail]
					length = head - tail + 1
				else:
					diff = diff + nums[i] - nums[tail]
					tail = tail + 1
					if diff >= 0:
						head = i
						while diff >= 0:
							diff = diff - nums[tail]
							tail = tail + 1
						tail = tail - 1
						diff = diff + nums[tail]
						length = head - tail + 1
		return length
    
if __name__ == '__main__':
    x = Solution()
    print(x.minSubArrayLen(int(input()),eval(input())))