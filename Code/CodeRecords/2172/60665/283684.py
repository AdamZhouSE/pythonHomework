class Solution:
	
	def isOpe(self,s):
		if s == '+' or s == '-':
			return 1
		elif s == '*' or s == '/':
			return 2
		elif s == '^':
			return 3
		elif s == '(':
			return 4
		elif s == ')':
			return 0
		else:
			return -1
	
	def fromStack(self, s):
		if s == '(':
			return 0
		else:
			return self.isOpe(s)
	
	def infixToPos(self, S):
		stack = [0] * len(S)
		dataTop = -1
		opeTop = len(S)
		look1 = stack[dataTop+1]
		look2 = stack[opeTop-1]
		
		index = 0
		while index < len(S):
			ch = S[index]
			if self.isOpe(S[index]) == -1:
				operator = S[index]
				while index + 1 < len(S) and self.isOpe(S[index+1])==-1:
					index += 1
					operator += S[index]
				dataTop += 1
				stack[dataTop] = operator
			else:
				if opeTop == len(S):
					opeTop -= 1
					stack[opeTop] = S[index]
				else:
					while opeTop < len(stack) and self.isOpe(S[index]) <= self.fromStack(stack[opeTop]):
						if stack[opeTop] != '(':
							stack[dataTop - 1] = stack[dataTop - 1] + stack[dataTop] + stack[opeTop]
							dataTop -= 1
							opeTop += 1
						else:
							opeTop += 1
							break
					if S[index] != ')':
						opeTop -= 1
						stack[opeTop] = S[index]
			index += 1
						
		while opeTop != len(S):
			stack[dataTop - 1] = stack[dataTop - 1] + stack[dataTop] + stack[opeTop]
			dataTop -= 1
			opeTop += 1
			
		return stack[0]
	
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		print(x.infixToPos(input()))