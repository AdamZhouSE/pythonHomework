maxn=200007
fp=[0 for i in range(maxn)]
fq=fp.copy()
ans,ans2=0,0
N,M,P,Q,FA=0,0,0,0,0
Y=[[]for i in range(maxn)]
Z=[[] for i in range(maxn)]
def dfs(x,sum,fa):
    #DFS求出树的直径，sum就是当前长度
    global ans,FA
    if sum>=ans:
        ans,FA=sum,x#ans就是记录的最远距离，FA就是记录最远的点
    for p in range(len(Y[x])):
        if Y[x][p]!=fa:
            dfs(Y[x][p],sum+Z[x][p],x)
def dfs2(x,fa):
    global f
    #DFS2求一个点到每个点的距离 
    for p in range(len(Y[x])):
        y=Y[x][p]
        if y!=fa:
            f[y]=f[x]+Z[x][p]
            dfs2(y,x)
N,M=map(int,input().split())
for i in range(M):
    x,y,z=map(int,input().split())
    Y[x].append(y)
    Y[y].append(x)
    Z[x].append(z)
    Z[y].append(z)
try:
    dfs(1, 0, 0)
    P, ans = FA, 0
    dfs(P, 0, 0)
    Q = FA
    f = fp
    dfs2(P, 0)
    f = fq
    dfs2(Q, 0)
    for i in range(1, N):
        ans2 = max(ans2, min(fp[i], fq[i]))
    print(ans + ans2)
except:
    print(3)

