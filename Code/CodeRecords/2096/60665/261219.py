class Solution:
	def sqrt(self,n):
		i = 0
		while i**2 <= n:
			i = i+1
		return i - 1
	
if __name__ == '__main__':
    x = Solution()
    print(x.sqrt(int(input())))