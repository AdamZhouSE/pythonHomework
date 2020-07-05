class Solution:
	
	
	def search(self,tree, root, n):
		zig = []
		level = 0
		queue = [0] * n
		head = tail = divide = 0
		queue[tail] = root
		tail = (tail+1)%n
		while(head != tail):
			divide = tail
			level += 1
			temp = []
			print("Level {:d} :".format(level),end="")
			while(head != divide):
				temp.append(queue[head])
				print(" {:d}".format(queue[head]),end="")
				if tree[queue[head]][0] != 0:
					queue[tail] = tree[queue[head]][0]
					tail = (tail + 1) % n
				if tree[queue[head]][1] != 0:
					queue[tail] = tree[queue[head]][1]
					tail = (tail + 1) % n
				head = (head + 1) % n
			print()
			zig.append(temp)
			
		for i in range(len(zig)):
			if not i % 2 :
				print("Level {:d} from left to right:".format(i+1),end="")
				for j in range(len(zig[i])):
					print(" {:d}".format(zig[i][j]),end="")
				print()
			else:
				print("Level {:d} from right to left:".format(i + 1), end="")
				for j in range(len(zig[i])-1,-1,-1):
					print(" {:d}".format(zig[i][j]), end="")
				print()
				
				
				
if __name__ == '__main__':
	x = Solution()
	info = [int(i) for i in input().split()]
	n = info[0]
	tree = {}
	while info[0] > 0:
		info[0] -= 1
		node = [int(i) for i in input().split()]
		tree[node[0]] = node[1:]
	x.search(tree,info[1],n)