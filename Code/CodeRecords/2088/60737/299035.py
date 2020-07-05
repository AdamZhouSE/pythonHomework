N= 20
mp = [[0 for i in range(N)] for i in range(N)]
md = int(1e9+7)
n = int(input())
up=(1<<(n-1))-1
res = 0

def po(a, p):
    r = 1
    while p>0:
        if p&1:
            r = (r*a)%md
        p>>=1
        a = (a*a)%md
    return r

kir = [[0 for i in range(N)] for i in range(N)]
siz = [0]*262144
u, v = [[0 for i in range(N*N)] for i in range(N)], [[0 for i in range(N*N)] for i in range(N)]
m = [0]*N

def det():
    res, tr = 1, 0
    for i in range(1, n):
        if kir[i][i]==0:
            for j in range(i+1, n):
                if kir[j][i]==0:
                    continue
                tr^=1
                for k in range(1, n):
                    temp = kir[i][k]
                    kir[i][k] = kir[j][k]
                    kir[j][k] = temp
        for j in range(i, n):
            if kir[j][i]==0:
                continue
            div = po(kir[j][i], md-2)
            res = (res * kir[j][i])%md
            for k in range(i, n):
                kir[j][k] = (kir[j][k]*div)%md
        for j in range(i+1, n):
            if kir[j][i]==0:
                continue
            for k in range(i, n):
                kir[j][k]=(kir[j][k]+md-kir[i][k])%md
    for i in range(1, n):
        res*=kir[i][i]
    return res if tr==0 else (md-res)%md

for i in range(1, n):
    cmd = [int(j) for j in input().split( )]
    m[i] = cmd[0]
    for j in range(1, m[i]+1):
        u[i][j] = cmd[2*j-1]
        v[i][j] = cmd[2*j]
for i in range(1, up+1):
    siz[i] = siz[i>>1]+(i&1)
for i in range(1, up+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            kir[j][k] = 0
    j, p = 1, i
    while p:
        if p&1==0:
            continue
        for k in range(1, m[j]+1):
            U=u[j][k]
            V=v[j][k]
            kir[U][U]+=1
            kir[V][V]+=1
            kir[U][V]=(kir[U][V]+md-1)%md
            kir[V][U]=(kir[V][U]+md-1)%md
        p>>=1
        j+=1
    res=(res+md+(det() if (n-siz[i])%2 else -det()))%md
print(res)
