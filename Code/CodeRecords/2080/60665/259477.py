class Solution:
	edges = {}
	vertexes = []
	numOfV = 0
	
	def breadthFT(self,start):
		print(start,end="")
		queue = [start]
		queueTail = 0
		while len(queue) != self.numOfV:
			if queueTail == len(queue):
				for vertex in self.vertexes:
					if vertex not in queue:
						print(end=" ")
						print(vertex,end="")
						queue.append(vertex)
			while queueTail < len(queue):
				start = queue[queueTail]
				for i in range (0,self.numOfV):
					if self.edges[start][i] != '0':
						if self.vertexes[i] not in queue:
							print(end=" ")
							print(self.vertexes[i],end="")
							queue.append(self.vertexes[i])
				queueTail = queueTail + 1
		print()
		
	
	def driver(self):
		event = int(input())
		while event > 0:
			event = event - 1
			initial = input().split()
			self.numOfV = int(initial[0])
			start = initial[1]
			self.vertexes = input().split()
			for vertex in self.vertexes:
				self.edges[vertex] = input().split()[1:]
			
			self.breadthFT(start)
			
			
if __name__ == '__main__':
    x = Solution()
    x.driver()
		