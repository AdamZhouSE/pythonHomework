mod = 998244353
N = 300010
M = 60
V = [0 for i in range(2 * N)]
x = list(V)
al = [0 for i in range(N)]
dep = list(al)
fa = [[0 for i in range(22)] for j in range(N)]
book = list(al)
val = [[0 for i in range(M)] for j in range(N)]
mi = [0 for i in range(M)]
ct = 0


def add(u: int, v: int):
    global ct
    ct += 1
    V[ct] = v
    x[ct] = al[u]
    al[u] = ct


def dfs(u: int):  # 处理val的信息以及倍增的信息
    book[u] = True
    i = 0
    while fa[u][i]:
        fa[u][i+1] = fa[fa[u][i]][i]
        i += 1
    i = al[u]
    while i:
        if book[V[i]]:
            i = x[i]
            continue
        fa[V[i]][0] = u
        dep[V[i]] = dep[u] + 1
        for j in range(1, 51):
            mi[j] = mi[j-1] * dep[V[i]] % mod
        for j in range(1, 51):
            val[V[i]][j] = (mi[j] + val[u][j]) % mod
        dfs(V[i])
        i = x[i]


def lca(u: int, v: int):  # 倍增求lca
    if dep[u] < dep[v]:
        u = u + v
        v = u - v
        u = u - v
    d = dep[u] - dep[v]
    i = 0
    while d:
        if d & 1:
            u = fa[u][i]
        i += 1
        d >>= 1
    if u == v:
        return u
    for i in range(20, -1, -1):
        if fa[u][i] != fa[v][i]:
            u = fa[u][i]
            v = fa[v][i]
    return fa[u][0]


if __name__ == '__main__':
    n = eval(input())
    mi[0] = 1
    res = []
    for i in range(1, n):
        uv = input().split()
        u = int(uv[0])
        v = int(uv[1])
        add(u, v)
        add(v, u)
    dfs(1)  # dfs处理
    m = eval(input())
    for i in range(1, m+1):
        uvk = input().split()
        u = int(uvk[0])
        v = int(uvk[1])
        k = int(uvk[2])
        l = lca(u, v)  # 然后我们就直接减了，注意lca只算但是要算一次
        res.append((val[u][k] + val[v][k] + 2 * mod - val[fa[l][0]][k] - val[l][k]) % mod)
    for r in res:
        print(r)