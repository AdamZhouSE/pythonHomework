class Solution:
	def count(self, s):
		n = 3
		res = 0
		while n <= len(s):
			count = [0] * 3
			left = right = 0
			for i in range(len(s)):
				if right - left < n:
					count[s[i]] += 1
					right += 1
					while count[s[i]] > n//3:
						count[s[left]] -= 1
						left += 1
				if right - left == n:
					res += 1
					count[s[left]] -= 1
					left += 1
			n += 3
		return res
	
if __name__ == '__main__':
	x = Solution()
	T = int(input())
	while T > 0:
		T -= 1
		s = input()
		print(x.count([int(i) for i in s]))