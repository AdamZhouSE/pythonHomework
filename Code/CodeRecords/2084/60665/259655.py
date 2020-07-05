class Solution:
	bridges = {}
	islands = 0
	
	def findSafestPath(self, x, y):
		MAX_INT = 10 ** 10
		safePoints = [MAX_INT] * self.islands
		safePoints[x] = 0
		routine = [-1] * self.islands
		routine[0] = x
		
		for i in range(0, self.islands):
			minSP = MAX_INT
			for j in range(0, self.islands):
				if j not in routine:
					if (routine[i], j) in self.bridges:
						safePoints[j] = min(self.bridges[(routine[i], j)] + safePoints[routine[i]],safePoints[j])
					if safePoints[j] < minSP:
						minSP = safePoints[j]
						routine[i + 1] = j
			if minSP == MAX_INT:
				return -1
			if routine[i + 1] == y:
				return safePoints[y]
	
	def driver(self):
		initial = input().split()
		self.islands = int(initial[0])
		numOfB = int(initial[1])
		start = int(initial[2]) - 1
		end = int(initial[3]) - 1
		while numOfB > 0:
			numOfB = numOfB - 1
			bridge = input().split()
			x = int(bridge[0]) - 1
			y = int(bridge[1]) - 1
			length = int(bridge[2])
			if (x,y) in self.bridges:
				if length<self.bridges[(x,y)]:
					self.bridges[(x, y)] = self.bridges[(y, x)] = length
			else:
				self.bridges[(x,y)] = self.bridges[(y,x)] = length
		
		print(self.findSafestPath(start,end))


if __name__ == '__main__':
	x = Solution();
	x.driver();
	