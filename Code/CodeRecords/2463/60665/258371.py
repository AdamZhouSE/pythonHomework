class Solution:
	def twoSum(self, numbers: [int], target: int) -> [int]:
		start, end = 0, len(numbers) - 1
		while start != end:
			sum = numbers[start] + numbers[end]
			if sum == target:
				return [start+1,end+1]
			elif sum < target:
				start = start + 1
			else:
				end = end - 1
		return
	
	
if __name__ == '__main__':
    x = Solution()
    print(x.twoSum(eval(input()),int(input())))