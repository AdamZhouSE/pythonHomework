class Solution:
	def evalExp(self, S):
		data = [0] * len(S)
		top = -1
		for ele in S:
			if ele == '+':
				data[top - 1] = data[top - 1] + data[top]
				top -= 1
			elif ele == '-':
				data[top - 1] = data[top - 1] - data[top]
				top -= 1
			elif ele == '*':
				data[top - 1] = data[top - 1] * data[top]
				top -= 1
			elif ele == '/':
				data[top - 1] = data[top - 1] // data[top]
				top -= 1
			else:
				top += 1
				data[top] = int(ele)
				
		return data[top]
	
if __name__ == '__main__':
	n = int(input())
	x = Solution()
	while n > 0:
		n -= 1
		print(x.evalExp(input()))