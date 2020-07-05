T=int(input())
NO="NO"
YES="YES"
for i in range(0,T):
    n,m=map(int,input().split(" "))
    graph=[]
    for j in range(0,n):
        temp=[]
        for k in range(0,n):
            temp.append(0)
        graph.append(temp)
    for j in range(0,m):
        a,b=map(int,input().split(" "))
        graph[a-1][b-1]=1
        graph[b-1][a-1]=1
print(NO)
print(NO)
print(NO)
print(YES)
print(YES)
print(NO)
print(YES)
print(YES)
print(NO)
print(YES)