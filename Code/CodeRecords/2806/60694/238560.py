cost, f = 0, float('inf')
for i in range(int(input())):
	n, m = map(int,input().split())
	f = min(f,m)
	cost+=f*n
print(cost)