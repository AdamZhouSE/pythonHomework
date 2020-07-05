class TreeNode:
	name = ''
	left = right = None
	count = 1
	depth = 1
	
	def __init__(self, name, depth, count = 1):
		self.name = name
		self.depth = depth
		self.count = count

class Solution:
	appearK = {}
	maxTimes = 0
	length = -1
	
	def dfsSearch(self, root, k):
		if root is None:
			return
		else:
			if root.count == k:
				self.appearK[root.depth] = self.appearK.get(root.depth, 0) + 1
				if self.maxTimes < self.appearK[root.depth]:
					self.maxTimes = self.appearK[root.depth]
					self.length = root.depth
				elif self.maxTimes == self.appearK[root.depth]:
					self.length = max(self.length, root.depth)
			self.dfsSearch(root.left, k)
			self.dfsSearch(root.right, k)
	
	def matchSub(self, s, k):
		treeRoot = TreeNode(s[0], 1, 0)
		for i in range(len(s)):
			root = treeRoot
			for j in range(i, len(s)):
				while s[j] != root.name and root.right is not None:
					root = root.right
					
				if s[j] == root.name:
					root.count += 1
					if root.left is None and i + 1 < len(s):
						root.left = TreeNode(s[j], root.depth + 1, 0)
					root = root.left
				else:
					root.right = TreeNode(s[j], root.depth)
					root = root.right
					if j + 1 < len(s):
						root.left = TreeNode(s[j + 1], root.depth + 1, 0)
						root = root.left
		
		self.length = -1
		self.maxTimes = 0
		self.appearK = {}
		self.dfsSearch(treeRoot, k)
		
		return self.length
		
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		info = input().split()
		print(x.matchSub(info[0], int(info[1])))