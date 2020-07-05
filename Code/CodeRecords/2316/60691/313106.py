N = 100
INF = 1000000007
n = 0
a = [[0 for i in range(N)] for j in range(N)]
b = [[0 for i in range(N)] for j in range(N)]
link = [0]*N
lx = [0.0]*N
ly = [0.0]*N
W = [[0 for i in range(N)] for j in range(N)]
visx = [False]*N
visy = [False]*N
def dfs(x:int):
    visx[x] = True
    for y in range(1,n+1):
        if (not visy[y]) and (ly[x]+ly[y]-W[x][y]==0.0):
            visy[y] = True
            if(link[y]==-1 or dfs(link[y])):
                link[y] = x
                return True
    return False
def KM():
    for i in range(1,n+1):
        lx[i] = -INF
        for j in range(1,n+1):
            lx[i] = max(lx[i],W[i][j])
    for i in range(1,n+1):
        while(1):
            if dfs(i): break
            d = INF
            for x in range(1,n+1):
                if visx[x]:
                    for y in range(1,n+1):
                        if not visy[y]:
                            d = min(d,lx[x]+ly[y]-W[x][y])
            if d==INF:return -1
            for x in range(1,n+1):
                if visx[x]:
                    lx[x]-=d
            for y in range(1,n+1):
                if visy[y]:
                    ly[y]+=d
    res = 0.0
    for i in range(1,n+1):
        if link[i]>-1:
            res+=W[link[i]][i]
    return res>0.0

def reset(m):
    for i in range(1,n+1):
        for j in range(1,n+1):
            W[i][j] = 1.0*a[i][j]-m*b[i][j]
n = eval(input())
for i in range(1,n+1):
    line = input().split(' ')
    for j in range(1,n+1):
        a[i][j] = int(line[j-1])
for i in range(1,n+1):
    line = input().split(' ')
    for j in range(1,n+1):
        b[i][j] = int(line[j-1])
l = 0.0
r = 1e4
m = 0.0
while r-l>=1e-8:
    m = l+(r-l)/2
    reset(m)
    if KM():
        l = m
    else:r = m
print('{0:.6f}'.format(float(m)))