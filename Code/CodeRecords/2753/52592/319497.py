import collections
class Solution:
	def findCheapestPrice(self, n, flights, src, dst, K):
		# K => bfs
		if flights == [] or src == dst : return 0 # special case
		queue = collections.deque([(src, 0)])
		cost = [float('inf')] * n
		cost[src] = 0
		adjList = collections.defaultdict(list)
		costList = collections.defaultdict(tuple)
		for x, y, c in flights:
			adjList[x].append(y)
			costList[(x, y)] = c
			
		for _ in range(K + 1):
			length = len(queue)
			for i in range(length):
				top, c = queue.popleft()
				for nei in adjList[top]:
					if costList[(top, nei)] + c < cost[nei]:
						cost[nei] = costList[(top, nei)] + c
						queue.append((nei, cost[nei]))
		return cost[dst] if cost[dst] != float('inf') else -1


n=int(input());
flights=input();
src=int(input());
dst=int(input());
k=int(input());
flights=flights.replace("[","")
flights=flights.replace("]","")
list1=[]
listm=flights.split(",")
list2=[]
for i in range(9):
    list2.append(int(listm[i]))
list3=[]
for i in range(3):
    for j in range(3):
        list3.append(list2[i*3+j])
    list1.append(list3)
    list3=[]
s=Solution()
res=s.findCheapestPrice(n,list1,src,dst,k)
print(res)