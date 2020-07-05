info=input().split()
n=int(info[0])
m=int(info[1])
L=int(info[2])
colors=[0]*(n+1)
src=input().split()
for i in range(1,n+1):
    colors[i]=int(src[i-1])
graph=[[0]*(n+1) for i in range(n+1)]


def findpath(start,end,before,fr):
    if start==end:
        return before
    ans=10000
    for v in range(1,n+1):
        if graph[start][v]>0 and v not in fr:
            tmp=max(graph[start][v],before)
            fr.append(start)
            ans=min(findpath(v,end,tmp,fr),ans)
            fr.remove(start)
    return max(ans,before)


for i in range(m):
    edge=input().split()
    x=int(edge[0])
    y=int(edge[1])
    v=int(edge[2])
    graph[x][y]=graph[y][x]=v
sum=0
for i in range(1,n):
    for j in range(i+1,n+1):
        if abs(colors[i]-colors[j])>=L:
            sum+=findpath(i,j,0,[])
print(sum)