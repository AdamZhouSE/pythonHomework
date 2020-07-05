T=int(input())
for i in range(0,T):
    n,m,k=map(int,input().split(" "))
    graph=[]
    for j in range(0,n):
        temp=[]
        for k in range(0,n):
            temp.append(10000)
        graph.append(temp)
    thing=map(int,input().split(" "))
    for j in range(0,m):
        a,b,c=map(int,input().split(" "))
        graph[a-1][b-1]=c
        graph[b-1][a-1]=c
    start,end=map(int,input().split(" "))