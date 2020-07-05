class Solution:
	def findMST(self,vertexes:set, edges:[[int]]):
		MAX_INT = 10**10
		n = len(vertexes)
		minDist = [MAX_INT]*n
		for i in range(0,n):
			minDist[i] = edges[0][i]
		minDist[0] = -1
		vertexes.discard(0)
		
		res = 0
		while len(vertexes) != 0:
			mini = MAX_INT
			next = -1
			for num in vertexes:
				if minDist[num] < mini:
					mini = minDist[num]
					next = num
			
			if next == -1:
				return -1
			
			vertexes.discard(next)
			minDist[next] = -1
			res = res + mini
			for num in vertexes:
				minDist[num] = min(minDist[num], edges[next][num])
			
		return res
	
	def driver(self):
		MAX_INT = 10**10
		
		initial = input().split()
		numOfV = int(initial[0])
		numOfE = int(initial[1])
		vertexes = set()
		edges = []
		for i in range(0,numOfV):
			vertexes.add(i)
			edges.append([MAX_INT]*numOfV)
		
		while  numOfE > 0:
			numOfE = numOfE - 1
			edge = input().split()
			x = int(edge[0]) - 1
			y = int(edge[1]) - 1
			length = int(edge[2])
			edges[x][y] = edges[y][x] = min(length,edges[x][y])
		
		print(self.findMST(vertexes,edges),end="")
		
if __name__ == '__main__':
    x = Solution()
    x.driver()