def search_ring(x):
    global visited,n
    flag=False
    for i in range(1,n):# 都是从0搜的0是根不考虑
        if edge[x][i]:
            if visited[i]==-1:
                visited[i]=x
                flag=search_ring(i)
            elif visited[x]!=i:
                return True
        if flag:
            return True
    return False
            
ee=eval(input())
n=len(ee)
edge=[[False for i in range(0,n)]for i in range(0,n)]
repeated=False
for i in range(0,n):
    if edge[ee[i][0]-1][ee[i][1]-1]==True:
        repeated=True
        print(ee[i])
        break
    else:
        edge[ee[i][0]-1][ee[i][1]-1]=True
        edge[ee[i][1]-1][ee[i][0]-1]=True
if not repeated:
    for i in range(n-1,-1,-1):
        visited=[-1 for i in range(0,n)]
        edge[ee[i][0]-1][ee[i][1]-1]=False
        edge[ee[i][1]-1][ee[i][0]-1]=False
        ring=search_ring(0)
        edge[ee[i][0]-1][ee[i][1]-1]=True
        edge[ee[i][1]-1][ee[i][0]-1]=True
        if not ring:
            print(ee[i])
            break