class Solution:
	def balance(self, S):
		if len(S) % 2 == 1:
			return -1
		
		res = 0
		if S[0] == '}':
			S = "{" + S[1:]
			res += 1
		if S[len(S)-1] == '{':
			S = S[:len(S)-1] + "}"
			res += 1
			
		n1 = n2 = 0
		for ele in S:
			if ele == "{":
				n1 += 1
			else:
				n2 += 1
		
		return abs(n1 - n2) // 2 + res

if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		print(x.balance(input()))