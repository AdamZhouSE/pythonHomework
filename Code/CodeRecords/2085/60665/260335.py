class Solution:
	def findSST(self, numOfV, edges, root):
		res = 0
		MAX_INT = int(2**31 -1 )
		
		while True:
			shortestIn = [MAX_INT]*numOfV
			union = [-1]*numOfV
			# 遍历边得到各点最小入边，建立相应并查集
			for edge in edges.keys():
				if edge[1] == edge[0]:
					continue
				if shortestIn[edge[1]] > edges[edge]:
					union[edge[1]] = edge[0]
					shortestIn[edge[1]] = edges[edge]
			
			for i in range(0,numOfV):
				if i == root:
					continue
				# 出现除根外的孤立点，无最小树形图
				if shortestIn[i] == MAX_INT:
					return -1
				# 记录权值
			
			count = 0
			shortestIn[root] = 0
			# vis判定点是否在同一有向环路，id为有向环或单独点在缩聚后新图的标记
			vis = [-1]*numOfV
			id = [-1]*numOfV
			for  i in range(0,numOfV):
				res = res + shortestIn[i]
				
				y = i
				# 遍历到根或者点已属于其他环或者找到环路时退出
				while y!=root and vis[y]!=i and id[y]==-1:
					vis[y] = i
					y = union[y]
				# 找到新环路，以count标记
				if y!=root and id[y]==-1:
					id[y] = count
					x = union[y]
					while x != y:
						id[x] = count
						x = union[x]
					count = count + 1
			# 无环，输出最小树形图权值
			if count == 0:
				break
			
			# 标记剩余单独点
			for i in range(0,numOfV):
				if id[i] == -1:
					id[i] = count
					count = count + 1
			
			# 更新新图的边，点数，根
			newEdges = {}
			for edge in edges.keys():
				x = id[edge[0]]
				y = id[edge[1]]
				if x != y:
					if (x,y) in newEdges:
						newEdges[(x,y)] = min(newEdges[(x,y)],edges[edge] - shortestIn[edge[1]])
					else:
						newEdges[(x,y)] = edges[edge] - shortestIn[edge[1]]
			edges = newEdges
			numOfV = count
			root = id[root]
			
		return res
			
	def driver(self):
		initial = input().split()
		numOfV = int(initial[0])
		numOfE = int(initial[1])
		root = int(initial[2]) - 1
		edges = {}
		while numOfE > 0:
			numOfE = numOfE - 1
			edge = input().split()
			x = int(edge[0]) - 1
			y = int(edge[1]) - 1
			length = int(edge[2])
			if x == y:
				continue
			if (x,y) in edges:
				edges[(x,y)] = min(edges[(x,y)],length)
			else:
				edges[(x,y)] = length
		print(self.findSST(numOfV,edges,root),end="")
		
if __name__ == '__main__':
    x = Solution()
    x.driver()