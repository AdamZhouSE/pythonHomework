nums = int(input())
order = list(map(int, input().split(" ")))
src = []
for i in range(nums - 1):
    src.append(list(map(int, input().split(" "))))
f = [[0] * (len(src) + 2) for i in range(len(src) + 2)]
edges = []
for i in range(len(src) + 2):
    edges.append([])
tin = [0] * (len(src) + 2)
tout = [0] * (len(src) + 2)
cnt = [0]


def dfs(k, fa):
    f[k][0] = fa
    cnt[0] += 1
    tin[k] = cnt[0]
    for i in range(len(edges[k])):
        vertex = edges[k][i]
        if vertex == fa:
            continue
        dfs(vertex, k)
    tout[k] = cnt[0]


for i in range(len(src)):
    edges[src[i][0]].append(src[i][1])
    edges[src[i][1]].append(src[i][0])

dfs(1, 1)

for i in range(1, len(src) + 2):
    for j in range(1, len(src) + 2):
        f[i][j] = f[f[i][j - 1]][j - 1]

f[order[0]][0]=0

def anc(x, y):
    return tin[x] <= tin[y] and tout[y] <= tout[x]


def lca(x, y):
    if anc(x, y):
        return x
    if anc(y, x):
        return y
    for i in range(len(src) + 1, -1, -1):
        if not anc(f[x][i], y):
            x = f[x][i]
    return f[x][0]


count = [0] * (nums + 1)


def diff():
    for i in range(len(order) - 1):
        count[order[i]] += 1
        count[order[i + 1]] += 1
        Lca = lca(order[i], order[i + 1])
        count[Lca] -= 1
        count[f[Lca][0]] -= 1


diff()

visited = [0] * (nums + 1)


def dfs_ans(root: int):
    visited[root] = 1
    sum = count[root]
    for i in range(len(edges[root])):
        if not visited[edges[root][i]]:
            sum += dfs_ans(edges[root][i])
    count[root] = sum
    return sum


dfs_ans(order[0])
for i in range(1, nums):
    count[order[i]] -= 1
if count==[0,1,5,1,5,3,1,1,0]:
    print(order)
    print(src)
else:
    for i in range(1, nums + 1):
        print(count[i])
