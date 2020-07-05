maxn = int(2e5 + 7)
head, nex, to, val, tot, n, dat = [0]*maxn, [0]*maxn, [0]*maxn, [0]*maxn, 0, 0, [0]*maxn

def init():
    global head, tot
    for i in range(1, 2*n):
        head[i] = 0
    tot = 0


def add(x, y, z):
    global tot, to, nex, val, head
    tot += 1
    to[tot] = y
    nex[tot] = head[x]
    val[tot] = z
    head[x] = tot


def dfs(u, fa):
    global to, val, nex, head, dat
    i = head[u]
    while i:
        v = to[i]
        w = val[i]
        if v == fa:
            i = nex[i]
            continue
        dat[v] = dat[u] ^ w
        dfs(v,u)
        i = nex[i]


if __name__ == "__main__":
    n = int(input())
    init()
    for i in range(n-1):
        cmd = [int(k) for k in input().split( )]
        x, y, z = cmd[0], cmd[1], cmd[2]
        add(x,y,z)
        add(y,x,z)
    dfs(1,-1)
    q = int(input())
    while q:
        cmd = [int(k) for k in input().split( )]
        x, y = cmd[0], cmd[1]
        print(dat[x] ^ dat[y])
        q -= 1



