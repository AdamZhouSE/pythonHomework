class Solution:
	def index(self, k):
		n = 1
		while k > 2**(n+1) - 2:
			n += 1
		n -= 1
		k -= 2**(n+1) - 2
		
		res = []
		while n >= 0:
			if k > 2**n:
				res.append('7')
			else:
				res.append('4')
			k = (k-1)%2**n + 1
			n -= 1
		
		return ''.join(res)
	

if __name__ == '__main__':
	n = int(input())
	x = Solution()
	while n > 0:
		n -= 1
		k = int(input())
		print(x.index(k))