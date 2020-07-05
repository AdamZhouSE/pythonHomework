class Solution:
	def isUgly(self,num):
		if num <= 0:
			return False
		for n in [2,3,5]:
			while num % n == 0:
				num = num // n
		return num == 1
	
if __name__ == '__main__':
    x = Solution()
    print(x.isUgly(int(input())))