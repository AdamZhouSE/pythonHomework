def dfs(r, fa):
    father[r][0] = fa
    cnt[0] += 1
    tin[r] = cnt[0]
    for e in edges[r]:
        if e == fa:
            continue
        dfs(e, r)
    tout[r] = cnt[0]


def anc(x, y):
    return tin[x] <= tin[y] and tout[y] <= tout[x]


def lca(x, y):
    if anc(x, y):
        return x
    if anc(y, x):
        return y
    for i in range(n, 0, -1):
        if not anc(father[x][i], y):
            x = father[x][i]
    return father[x][0]


def add_weight(x, y, z):
    a = lca(x, y)
    count[x] += 1
    count[y] += 1
    count[a] -= 1
    count[father[a][0]] -= 1
    if a==root:
        dfs_ans(a)
    else:
        dfs_ans(father[a][0])
    for i in range(1, n + 1):
        vertex[i] += count[i] * z


def dfs_ans(root):
    sum = count[root]
    for e in edges[root]:
        if e !=father[root][0]:
            sum += dfs_ans(e)
    count[root] = sum
    return sum


def add_sub(x,z):
    vertex[x]+=z
    for e in edges[x]:
        if e!=father[x][0]:
            add_sub(e,z)
    return


def dfs_sum(root):
    sum=vertex[root]
    for e in edges[root]:
        if e!=father[root][0]:
            sum+=dfs_sum(e)
    return sum



def dis(x):
    d=0
    while x!=root:
        d+=vertex[x]
        x=father[x][0]
    return d


def path_sum(x,y):
    a=lca(x,y)
    return dis(x)+dis(y)-dis(a)


if __name__ == '__main__':
    n, operator, root, mod = map(int, input().strip().split(" "))
    vertex = [0] + list(map(int, input().strip().split(" ")))
    edges = []
    for i in range(n + 1):
        edges.append([])
    for i in range(n - 1):
        edge = list(map(int, input().split(" ")))
        edges[edge[0]].append(edge[1])
        edges[edge[1]].append(edge[0])
    father = [[0] * (n + 1) for i in range(n + 1)]

    cnt = [0]
    tin = [0] * (n + 1)
    tout = [0] * (n + 1)

    dfs(root, root)

    for j in range(1, n + 1):
        for i in range(1, n + 1):
            father[i][j] = father[father[i][j - 1]][j - 1]

    father[root][0] = 0

    count = [0] * (n + 1)

    for i in range(operator):
        op=list(map(int,input().split(" ")))
        if op[0]==1:
            add_weight(op[1],op[2],op[3])
        elif op[0]==2:
            print(path_sum(op[1],op[2])%mod)
        elif op[0]==3:
            add_sub(op[1],op[2])
        elif op[0]==4:
            print(dfs_sum(op[1])%mod)
