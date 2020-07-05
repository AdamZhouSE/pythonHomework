class Solution:
	def lcp(self,s1,s2):
		res = 0
		for i in range(0,min(len(s1),len(s2))):
			if s1[i] == s2[i]:
				res += 1
			else:
				break
		return res
	
	def ljj(self,s):
		
		for i in range(0,len(s)):
			if i < 2:
				print(0)
				continue
			secret = 0
			for j in range(1,i):
				for m in range(0,j):
					lcp = self.lcp(s[j:i+1],s[m:i+1])
					while lcp > 1 and (m + lcp) > j:
						secret += lcp
						lcp = lcp - 1
			print(secret)
			

if __name__ == '__main__':
    x = Solution()
    x.ljj(input())