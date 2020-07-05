class Solution:
	def largestDivisibleSubset(self, nums: [int]) -> [int]:
		if not nums:
			return []
		nums.sort()
		length = len(nums)
		pre = [-1]*length
		scale = [1]*length
		
		maxLength = 1
		index = 0
		for i in range(0,length):
			for j in range(0,i):
				if nums[i] % nums[j] == 0:
					if scale[i] < scale[j] + 1:
						scale[i] = scale[j] + 1
						pre[i] = j
						if scale[i] > maxLength:
							maxLength = scale[i]
							index = i
		
		res = [0] * maxLength
		while maxLength > 0:
			maxLength = maxLength - 1
			res[maxLength] = nums[index]
			index = pre[index]
			
		return res
	
	
if __name__ == '__main__':
    x = Solution()
    print(x.largestDivisibleSubset(list(eval(input()))))