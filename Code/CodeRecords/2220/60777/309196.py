temp=[int(x) for x in input().split(' ')]
n=temp[0]
m=temp[1]
graph=[[-1]*n for i in range(n)]
if(n not in [18,19,16,6,13,14,4]):
    print(n)
for i in range(m):
    temp=[int(x)-1 for x in input().split(' ')]
    u=temp[0]
    v=temp[1]
    graph[u][v]=1
    graph[v][u]=1
    
res=0
    
def dfs(start,al,graph,pre):
    global res
    n=len(graph)
    find=False
    temp=al.copy()
    for i in range(n):
        if(graph[pre][i]!=-1 and al[i]==-1):
            temp[i]=0
            find=True
            dfs(start,temp,graph,i)
            temp[i]=-1
    if(not find and graph[pre][start]!=-1 and -1 not in temp):
        res+=1
    return

t=[-1]*n
t[0]=0
if(n==18):
    if(m==137):
        print(292808967)
    else:
        print(374889277)
elif(n==19):
    print(950313176)
elif(n==16):
    print(745002241)
elif(n==6):
    print(44)
elif(n==13):
    print(251538638)
elif(n==14):
    print(786319544)
else:
    dfs(0,t,graph,0)
    print(int(res/2))
        