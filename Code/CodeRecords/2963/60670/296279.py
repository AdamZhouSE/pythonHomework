def ishui(strr):
    l=0
    r=len(strr)-1
    while l<=r:
        if strr[l]!=strr[r]:
            return False
        l+=1
        r-=1
    return True

def dfs(now,target,strr):
    global used,edge,n,cnt
    if now==target and ishui(strr):
        cnt+=1
    used[now]=True
    for i in range(0,n):
        if edge[now][i]!=None and (not used[i]):
            dfs(i,target,strr+edge[now][i])

n=int(input())
edge=[[None for i in range(0,n)] for i in range(0,n)]
for i in range(0,n-1):
    line=input().split()
    x=int(line[0])-1
    y=int(line[1])-1
    edge[x][y]=line[2]
    edge[y][x]=line[2]
cnt=0
for i in range(0,n):
    for j in range(i+1,n):
        used=[False for i in range(0,n)]
        dfs(i,j,'')
print(cnt)
