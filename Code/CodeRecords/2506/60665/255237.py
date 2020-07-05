class Solution:
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
		return res;
	
	
if __name__ == '__main__':
    x = Solution();
    nums = eval(input());
    print(x.lengthOfLIS(nums))