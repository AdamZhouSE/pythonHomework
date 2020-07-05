class Solution:
	def subset(self, S, k):
		table = {}
		maxLength = 0
		
		length = 0
		left = 0
		for i, ele in enumerate(S):
			if ele in table or len(table) < 3:
				length += 1
				table[ele] = i
			else:
				index = min(table.values())
				table.pop(S[index])
				table[ele] = i
				length -= (index - left)
				left = index + 1
				
			maxLength = max(maxLength, length)
			
		return maxLength
	
if __name__ == '__main__':
	n = int(input())
	x = Solution()
	while n > 0:
		n -= 1
		s = input()
		k = int(input())
		print(x.subset(s, k))