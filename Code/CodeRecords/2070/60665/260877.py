class Solution:
	def pow(self,num,n):
		if n==0:
			return 1
		if n < 0:
			num = 1.0/num
			n = - n
			
		res = 1
		while n != 0:
			if n % 2 == 1:
				res = res * num
			num = num ** 2
			n = n // 2
		return res
	
if __name__ == '__main__':
    x = Solution()
    res = x.pow(eval(input()),eval(input()))
    print("{:.5f}".format(res))