class Solution:
	table = {}
	def createRule(self, S):
		for i, ele in enumerate(S):
			self.table[ele] = i
	
	def rule(self, s):
		return self.table.get(s, -1)
	
	def customSortString(self, S, T):
		self.createRule(S)
		res = sorted(T, key=lambda x: self.rule(x))
		return "".join(res)
	

if __name__ == '__main__':
	x = Solution()
	S = input()
	T = input()
	print(x.customSortString(S, T))