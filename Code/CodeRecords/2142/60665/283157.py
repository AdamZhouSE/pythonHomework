class Solution:
	def parentheses(self, exp):
		stack = [0]*len(exp)
		res = []
		top = -1
		count = 1
		
		for ele in exp:
			if ele == '(':
				top += 1
				stack[top] = count
				res.append(count)
				count += 1
			elif ele == ')':
				if top != -1:
					res.append(stack[top])
					top -= 1
		
		return res
	
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		res = x.parentheses(input())
		for ele in res:
			print(ele,end=" ")
		print()