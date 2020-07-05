n=int(input())
loads=list(map(int,input().split(" ")))
edges=[[] for i in range(n)]
for i in range(n-1):
    x,y=map(int,input().split(" "))
    edges[x-1].append(y-1)
    edges[y-1].append(x-1)
result=[0 for i in range(n)]
    