class Solution:
# 等同于寻找最大上升子序列
	def lengthOfLIS(self,nums):
		tail,res = [0]*len(nums),0;
		for num in nums:
			if res == 0:
				tail[res] = num;
				res = res + 1;
			else:
				i,j = 0,res;
				while i < j:
					m = (i + j)//2;
					if tail[m] < num:
						i = m + 1;
					else:
						j = m;
				tail[i] = num;
				if res == j:
					res = res + 1;
		return len(nums) - res;
	
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		input()
		nums = [int(i) for i in input().split()]
		print(x.lengthOfLIS(nums))