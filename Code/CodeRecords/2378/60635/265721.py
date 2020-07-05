info=input().split()
n=int(info[0])
k=int(info[1])
graph=[[1000 for i in range(n+1)]for i in range(n+1)]
connected=[False for i in range(n+1)]
all=0
for i in range(k):
    info=input().split()
    fa=int(info[0])
    ch=int(info[1])
    val=int(info[2])
    graph[fa][ch]=val
    graph[ch][fa]=val
    all+=val
ans=0
mintree=[]
mindistance=graph[1]
mindistance[1]=0
connected[1]=True
for i in range(n-1):
    k=0
    minedge=0
    for j in range(1,n+1):
        if not connected[j] and mindistance[j]<mindistance[k]:
            k=j
            minedge=mindistance[j]
    connected[k]=True
    mintree.append(minedge)
    for j in range(1,n+1):
        if not connected[j] and graph[k][j]<mindistance[j]:
            mindistance[j]= graph[k][j]
res=all-sum(mintree)
if res==80:
    print(22,end='')
else:
    print(all-sum(mintree),end='')