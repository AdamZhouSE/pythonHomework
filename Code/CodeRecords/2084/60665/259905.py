class Solution:
	bridges = []
	islands = set()
	MAX_INT = 10 ** 10
	
	def findSafestPath(self, x, y):
		numOfI = len(self.islands)
		safePoints = [self.MAX_INT] * numOfI
		safePoints[x] = 0
		routine = [-1] * numOfI
		routine[0] = x
		self.islands.discard(x)
		
		for i in range(0, numOfI):
			minSP = self.MAX_INT
			for j in self.islands:
				safePoints[j] = min(self.bridges[routine[i]][j] + safePoints[routine[i]],safePoints[j])
				if safePoints[j] < minSP:
					minSP = safePoints[j]
					routine[i + 1] = j
			self.islands.discard(routine[i + 1])
			if minSP == self.MAX_INT:
				return -1
			if routine[i + 1] == y:
				return safePoints[y]
		
		
	def driver(self):
		initial = input().split()
		numOfI = int(initial[0])
		for i in range(0,numOfI):
			self.islands.add(i)
			self.bridges.append([self.MAX_INT]*numOfI)
		numOfB = int(initial[1])
		start = int(initial[2]) - 1
		end = int(initial[3]) - 1
		while numOfB > 0:
			numOfB = numOfB - 1
			bridge = input().split()
			x = int(bridge[0]) - 1
			y = int(bridge[1]) - 1
			length = int(bridge[2])
			if self.bridges[x][y] > length:
				self.bridges[x][y] = length
				self.bridges[y][x] = length
		
		print(self.findSafestPath(start,end))


if __name__ == '__main__':
	x = Solution();
	x.driver();
	