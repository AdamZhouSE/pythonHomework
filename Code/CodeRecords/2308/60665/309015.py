class Solution:
	def search(self, tree, root, n, target):
		stack = [0] * n
		top = -1
		mark = set()
		
		top += 1
		stack[top] = root
		state = 0
		
		while top != -1:
			temp = stack[top]
			if temp not in mark and tree[temp][0] != 0:
				mark.add(temp)
				top += 1
				stack[top] = tree[temp][0]
			else:
				if temp == target:
					state = 1
				elif state:
					print(temp)
					return
				if tree[temp][1] != 0:
					stack[top] = tree[temp][1]
				else:
					top -= 1
		
		print(0)
		
		
if __name__ == '__main__':
	x = Solution()
	info = [int(i) for i in input().split()]
	n = info[0]
	tree = {}
	while info[0] > 0:
		info[0] -= 1
		node = [int(i) for i in input().split()]
		tree[node[0]] = node[1:]
	
	x.search(tree,info[1],n,int(input()))