class Solution:
	table = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5,
				'G': 6, 'H': 7, 'I': 8, 'J': 9, 'K': 10, 'L': 11,
				'M': 12, 'N': 13, 'O': 14, 'P': 15, 'Q': 16,
				'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21,
				'W': 22, 'X': 23, 'Y': 24, 'Z': 25}
	
	def sortByAsc(self, s):
		if len(s) < 2:
			return s
		
		maxLength = 0
		minDiff = 26
		end = -1
		
		diff = 0
		count = 0
		for i in range(1, len(s)):
			if self.table[s[i]] - self.table[s[i-1]] == diff:
				count += 1
			else:
				if maxLength == count:
					minDiff = min(minDiff, diff)
					if minDiff == diff:
						end = i
				elif maxLength < count:
					maxLength = count
					minDiff = diff
					end = i
				count = 2
				diff = self.table[s[i]] - self.table[s[i-1]]
		if count != 2:
			if maxLength == count:
				minDiff = min(minDiff, diff)
				if minDiff == diff:
					end = len(s)
			elif maxLength < count:
				minDiff = diff
				end = len(s)
				
		return s[end-maxLength:end]
	
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		res = x.sortByAsc(input())
		for i in range(len(res)-1, -1, -1):
			print(res[i],end="")
		print()