class Solution:
	def longestValidParentheses(self, s: str) -> int:
		dp = [0] * len(s)
		res = 0
		for i in range(1, len(s)):
			if s[i] == ')':
				if s[i-1] == '(':
					if i >= 2:
						dp[i] = dp[i-2] + 2
					else:
						dp[i] = 2
				else:
					if i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
						if i - dp[i-1] - 2 >= 0 and s[i - dp[i-1] - 2] == ')':
							dp[i] = dp[i-1] + dp[i - dp[i-1] - 2] + 2
						else:
							dp[i] = dp[i-1] + 2
			res = max(res, dp[i])
			
		return res
	

if __name__ == '__main__':
	x = Solution()
	T = int(input())
	while T > 0:
		T -= 1
		s = input()
		print(x.longestValidParentheses(s))