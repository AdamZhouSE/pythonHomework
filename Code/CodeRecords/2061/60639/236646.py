from collections import deque 
N = 100005

gr = [[] for i in range(N)] 

def add_edge(u, v): 
	gr[u].append(v) 
	gr[v].append(u) 
def dijkstra(n): 
	vis = [0 for i in range(n)] 
	dist = [10**9 for i in range(n)] 
	vis[0] = 1
	dist[0] = 0
	q = deque() 
	q.append(0) 

	while (len(q) > 0): 
		x = q.popleft() 
		for i in gr[x]: 
			if (vis[i] == 1): 
				continue
			vis[i] = 1
			dist[i] = dist[x] + 1
			q.append(i) 
	return dist[n - 1] 

def Min_Moves(a, n): 
	fre = [[] for i in range(10)] 
	for i in range(n): 
		if (i != n - 1): 
			add_edge(i, i + 1) 
		fre[a[i]].append(i) 
	for i in range(10): 
		for j in range(len(fre[i])): 
			for k in range(j + 1,len(fre[i])): 
				if (fre[i][j] + 1 != fre[i][k] and
					fre[i][j] - 1 != fre[i][k]): 
					add_edge(fre[i][j], fre[i][k]) 
	return dijkstra(n) 
a = [1, 2, 3, 4, 1, 5] 
n = len(a) 
print(Min_Moves(a, n)) 


