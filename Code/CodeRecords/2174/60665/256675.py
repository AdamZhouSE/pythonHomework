class Solution:
	bridges = {}
	islands = 0
	
	def findSafestPath(self,x,y):
		MAX_INT = int(2**31 - 1)
		safePoints = [MAX_INT] * self.islands
		safePoints[x] = 0
		routine = [-1] * self.islands
		routine[0] = x
		
		for i in range(0,self.islands):
			minSP = MAX_INT
			for j in range(0,self.islands):
				if j not in routine:
					if (routine[i],j) in self.bridges:
						if self.bridges[(routine[i],j)]< safePoints[j]:
							safePoints[j] = max(self.bridges[(routine[i],j)],safePoints[routine[i]])
					if safePoints[j] < minSP:
						minSP = safePoints[j]
						routine[i+1] = j
			if minSP == MAX_INT:
				return -1
			if routine[i+1] == y:
				return safePoints[y]
				
		
	def driver(self):
		cmd = input().split()
		self.islands = int(cmd[0])
		eventsN = int(cmd[1])
		
		while eventsN > 0:
			eventsN = eventsN - 1;
			event = input().split()
			x = int(event[1])
			y = int(event[2])
			if event[0] == '0':
				self.bridges[(x,y)] = self.bridges[(y,x)] = int(event[3])
			elif event[0] == '1':
				self.bridges.pop((x,y))
				self.bridges.pop((y,x))
			elif event[0] == '2':
				print(self.findSafestPath(x,y));
		

if __name__ == '__main__':
    x = Solution();
    x.driver();