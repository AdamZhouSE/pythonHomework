class Solution:
	changeTable = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5,
	               'g': 6, 'h': 7, 'i': 8, 'j': 9, 'k': 10, 'l': 11,
	               'm': 12, 'n': 13, 'o': 14, 'p': 15, 'q': 16,
	               'r': 17, 's': 18, 't': 19, 'u': 20, 'v': 21,
	               'w': 22, 'x': 23, 'y': 24, 'z': 25}
	
	def countPuzzle(self, C, S):
		count = 0
		table = [0] * 26
		res = 0
		
		for le in S:
			table[self.changeTable[le]] += 1
		point = 0
		for i in range(len(C)):
			if i - point >= len(S):
				table[self.changeTable[C[point]]] += 1
				if table[self.changeTable[C[point]]] > 0:
					count -= 1
				point += 1
				
			table[self.changeTable[C[i]]] -= 1
			if table[self.changeTable[C[i]]] >= 0:
				count += 1
				
			if count == len(S):
				res += 1
		
		return res
	
	
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		C = input()
		S = input()
		print(x.countPuzzle(C, S))