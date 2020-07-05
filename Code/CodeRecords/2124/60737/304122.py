N, P = int(2e5+5), 1e9+7
nx = [0 for i in range(N)]
hd, V, sz, ls, s, dp, sn = [0]*N, [0]*N, [0]*N, [0]*N, [0]*N, [0]*N, [0]*N
a, g, pw = [0]*N, [0]*N, [0]*N
m, t, A, R, n, C = 0, 0, 0, 0, 0, 0


def add(u, v):
    global nx, hd, V, t
    t += 1
    nx[t] = hd[u]
    hd[u] = t
    V[hd[u]] = v


def dfs(x, fr):
    global sz, ls, s, dp, hd, nx, V, a, sn
    i = hd[x]
    while i > 0:
        if V[i] == fr:
            i = nx[i]
            continue
        if dp[V[i]]:
            s[x] = min(s[x], dp[V[i]])
        else:
            dfs(V[i], x)
            sn[x] += 1
            sz[x] ^= sz[V[i]]
            a[x] += 1 if s[V[i]] < dp[x] else 0
            s[x] = min(s[x], s[V[i]])
        i = nx[i]


def work(x, fr):
    global hd, nx, a, sn, A, sz, R, g, m, pw, n, C, dp, V
    w, u, z = 0, 0, 0
    y = 1 if fr > 0 else 0
    i = hd[x]
    while i>0:
        w += 1
        i = nx[i]
    if a[x] == sn[x]:
        v = A - sz[R] + (sz[R] ^ ls[x])
        if not v:
            g[x] = pw[m-w-n+1+C]
    else:
        i = hd[x]
        while i>0:
            if dp[V[i]] == dp[x]+1 and s[V[i]] >= dp[x]:
                u += sz[V[i]]
                z ^= sz[V[i]]
                y += 1
            i = nx[i]
        u += (sz[R]^z^ls[x])
        v = A-sz[R]+u
        if not v:
            g[x] = pw[m-w-n+1+C-1+y]
    i = hd[x]
    while i>0:
        if dp[V[i]]==dp[x]+1:
            work(V[i], x)
        i = nx[i]


if __name__ == "__main__":
    T = int(input())
    pw[0] = 1
    for i in range(1, N):
        pw[i] = (pw[i-1]*2)%P
    while T:
        cond = [int(i) for i in input().split( )]
        n, m = cond[0], cond[1]
        t, C, A = 0, 0, 0
        for i in range(1, n+1):
            hd[i] = 0
            s[i] = 0
            sn[i] = 0
            a[i] = 0
            dp[i] = 0
            g[i] = 0
        for i in range(m):
            cmd = [int(j) for j in input().split( )]
            x1, y1 = cmd[0], cmd[1]
            add(x1, y1)
            add(y1, x1)
            t = 0
        nums = list(input())
        for i in range(1, n+1):
            ls[i] = int(nums[i-1])
        for i in range(1, n+1):
            if not dp[i]:
                dfs(i, 0)
                A += sz[i]
                C += 1
        res1 = 0 if A else pw[m-n+C]
        print(res1, end="")
        for i in range(1, n+1):
            if dp[i] == 1:
                if not sn[i]:
                    if A == sz[i]:
                        g[i] = pw[m-n+C]
                else:
                    R = i
                    work(i, 0)
            print(" ", end="")
            print(g[i], end="")
        print()
        T -= 1
