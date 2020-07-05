s=[]
Limitpoint=1296+4
Limintn=18+2
for i in range(0,5):
    s.append([])
for ele in s:
    for j in range(0,20):
        ele.append([])
for ele in s:
    for subEle in ele:
        for i in range(0,40):
            subEle.append(0)
n=0
c=[]
for i in range(0, Limitpoint):
    c.append([])
for ele in c:
    for i in range(0, 4):
        ele.append(0)
vis=[]
for i in range(0, Limitpoint):
    vis.append([])
for ele in vis:
    for i in range(0, Limitpoint):
        ele.append(False)
f=[]
for i in range(0, Limitpoint):
    f.append([])
for ele in f:
    for i in range(0, 4):
        ele.append([])
for ele in f:
    for subEle in ele:
        for i in range(0,Limitpoint):
            subEle.append(0)
best=0
def init():
    global s
    global n
    n=int(input())
    for k in range(1, 5):
        for i in range(1, n+1):
            for j in range(1, i*2):
                s[k][i][j]=int(input())

def link(a, b):
    global vis
    global c
    if not vis[a][b]:
        vis[a][b]=True
        c[a][++c[a][0]]=b
    if not vis[b][a]:
        vis[b][a]=1
        c[b][++c[b][0]]=a

def make_graph():
    global n
    global s
    for k in range(1, 5):
        for i in range(2, n):
            for j in range(2, i*2-1):
                link(s[k][i][j], s[k][i][j-1])
                link(s[k][i][j], s[k][i][j+1])
                if j%2!=0:
                    link(s[k][i][j], s[k][i+1][j+1])
                else:
                    link(s[k][i][j], s[k][i-1][j-1])
    for k in range(1, 5):
        for j in range(2, n*2):
            link(s[k][n][j],s[k][n][j-1])
            link(s[k][n][j], s[k][n][j+1])
            link(s[k][n][j], s[k][n-1][j-1])
    k=1
    i=1
    while k<=n:
        link(s[1][i][1], s[3][i][i*2-1])
        link(s[1][i][i*2-1], s[2][i][1])
        link(s[2][i][i*2-1], s[3][i][1])
        k+=1
        i+=1
    for j in range(1, n*2, 2):
        link(s[1][n][j],s[4][n-(j/2)][1])
        link(s[2][n][j],s[4][j/2+1][((j/2)+1)*2-1])
        link(s[3][n][j],s[4][n][n*2-j])

def tree_max(i, limit1, limit2):
    global c
    global f
    start=1
    while c[i][start]!=limit2:
        start+=1
    if f[i][start][limit1]>0:
        return f[i][start][limit1]
    l=0
    r=0
    if limit1>limit2:
        l=limit2+1
        r=limit1
    else:
        l=limit1
        r=limit2-1
    lmax=0
    rmax=0
    for j in range(1, 4):
        if j!=start and (l<=c[i][j] and c[i][j]<=r):
            if c[i][j]<i:
                lmax=max(lmax,tree_max(c[i][j],l,i))
            else:
                rmax=max(rmax,tree_max(c[i][j],r,i))
    f[i][start][limit1]=lmax+rmax+1
    return f[i][start][limit1]

def dfs():
    global best
    global c
    best=0
    for i in range(1, n*n*4+1):
        lmax=0
        rmax=0
        for j in range(1, 4):
            if c[i][j]<i:
                lmax=max(lmax,tree_max(c[i][j],1,i))
            else:
                rmax=max(rmax,tree_max(c[i][j],n*n*4,i))
        best=max(best, lmax+rmax+1)
if __name__=='__main__':
    init()
    make_graph()
    dfs()
    print(best)
