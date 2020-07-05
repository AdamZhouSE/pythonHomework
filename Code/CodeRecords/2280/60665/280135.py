class Solution:
	def searchMssing(self, nums, N):
		if len(nums) == 0:
			return 1
		tortoise = 0
		res = N - 1
		while tortoise < len(nums):
			rabbit = nums[tortoise] - 1
			
			while rabbit != tortoise and rabbit != res:
				temp = rabbit
				rabbit = nums[rabbit] - 1
				nums[temp] = 0
			
			if rabbit == N - 1:
				res = tortoise
				
			tortoise += 1
			while tortoise < len(nums) and nums[tortoise] == 0:
				tortoise += 1
		
		return res + 1
	
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		N = int(input())
		nums = input().split()
		print(x.searchMssing([int(i) for i in nums], N))
		