class Solution:
	def palindrome(self):
		s = input().upper()
		i, j = 0, len(s) - 1
		while True:
			while i < j and not s[i].isalpha():
				i += 1
			while i < j and not s[j].isalpha():
				j -= 1
			if i >= j:
				return "YES"
			elif s[i] != s[j]:
				return "NO"
			else:
				i += 1
				j -= 1
	
	
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		print(x.palindrome())