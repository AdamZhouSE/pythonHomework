class Solution:
	s1 = ''
	s2 = ''
	K = 0
	def convert(self, s, t, l, r):
		earning = 0
		index = self.s1.find(self.s2[l-1:r],s-1)
		while index + (r-l) < t and index != -1:
			earning += self.K - (index + 1)
			index = self.s1.find(self.s2[l-1:r],index + (r-l)+1)
		
		return earning
	
if __name__ == '__main__':
	x = Solution()
	x.K = int(input().split()[1])
	x.s1 = input()
	x.s2 = input()
	n = int(input())
	while n > 0:
		n -= 1
		data = [int(i) for i in input().split()]
		print(x.convert(data[0], data[1], data[2], data[3]))