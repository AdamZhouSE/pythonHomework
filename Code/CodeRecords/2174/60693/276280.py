n_q=input().split();
n,q=int(n_q[0]),int(n_q[1])
bridges=[[-1 for i in range(n)] for i in range(n)]
def dfs(depth,start,end,cur,index,bridges,results:list,n,visited,path):
    if(start==end):
        results.append(max(path))
        return
    if(depth==n or index==n):
        return
    if(bridges[start][index]!=-1 and not visited[start][index]):
        path[cur]=bridges[start][index]
        visited[start][index]=1
        visited[index][start]=1
        dfs(depth+1,index,end,cur+1,0,bridges,results,n,visited,path)
    else:
        path=[-1 for _ in range(n)]
        dfs(depth,start,end,cur,index+1,bridges,results,n,visited,path)


def findSafestPath(bridges,x,y,n):
    result=[]
    path=[-1 for _ in range(n)]
    visited = [[0 for _ in range(n)] for _ in range(n)]
    dfs(0,x-1,y-1,0,0,bridges,result,n,visited,path)
    if len(result):return min(result)
    else:return -1

for _ in range(q):
    event=list(map(int,input().split()))
    if(event[0]==0):
        bridges[event[1]-1][event[2]-1]=event[3]
        bridges[event[2] - 1][event[1] - 1] = event[3]
    if(event[0]==1):
        bridges[event[1]-1][event[2]-1] = -1
        bridges[event[2]-1][event[1]-1] = -1
    if(event[0]==2):
        res=findSafestPath(bridges,event[1],event[2],n)
        print(res)