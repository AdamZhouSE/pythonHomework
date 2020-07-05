class Solution:
	def findSafe(self, n, k):
		nums = [i for i in range(1, n + 1)]
		nums[n - 1] = 0
		count = 0
		cur = -1
		while nums[cur] != (cur+n)%n:
			count += 1
			if count == k:
				nums[cur] = nums[nums[cur]]
				count = 0
			else:
				cur = nums[cur]
		
		return (cur+n)%n + 1
	
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		info = input().split()
		N = int(info[0])
		k = int(info[1])
		print(x.findSafe(N, k))