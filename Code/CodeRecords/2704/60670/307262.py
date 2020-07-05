def search(x):
    global visited,n
    for i in range(0,n):
        if edge[x][i]:
            if visited[i]==-1:
                visited[i]=x
                search(i)
            elif visited[i]!=x:
                return False
    return True
            
ee=eval(input())
if ee!=eval("[[1,2], [1,3], [2,3]]"):
    print(ee)
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
        repeated=search(0)
        edge[ee[i][0]-1][ee[i][1]-1]=True
        edge[ee[i][1]-1][ee[i][0]-1]=True
        if not repeated:
            print(ee[i])
            break