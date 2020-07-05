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
	
	def matchSub(self, s, k):
		treeRoot = TreeNode(s[0], 1, 0)
		dp = [0]*len(s)
		for i in range(len(s)):
			root = treeRoot
			for j in range(i, len(s)):
				while s[j] != root.name and root.right is not None:
					root = root.right
					
				if s[j] == root.name:
					if root.count == k:
						dp[root.depth-1] -= 1
					root.count += 1
					if root.count == k:
						dp[root.depth-1] += 1
					if root.left is None and j + 1 < len(s):
						root.left = TreeNode(s[j + 1], root.depth + 1, 0)
					root = root.left
				else:
					root.right = TreeNode(s[j], root.depth)
					root = root.right
					if root.count == k:
						dp[root.depth-1] += 1
					if j + 1 < len(s):
						root.left = TreeNode(s[j + 1], root.depth + 1, 0)
						root = root.left
		
		maxTimes = 1
		length = -1
		for i in range(len(s)):
			if dp[i] >= maxTimes:
				maxTimes = dp[i]
				length = i+1
		
		return length
		
if __name__ == '__main__':
	x = Solution()
	n = int(input())
	while n > 0:
		n -= 1
		info = input().split()
		print(x.matchSub(info[0], int(info[1])))