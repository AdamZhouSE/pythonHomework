lch = []
rch = []
f = []  # f[i]表示以i为根节点且包含i的最大连通块
ans = 1


def dfs(root):
    global ans
    if lch[root] == 0 and rch[root] == 0:
        f[root] = 1
        return
    if lch[root] != 0:
        dfs(lch[root])
    if rch[root] != 0:
        dfs(rch[root])
    if lch[root] < root:
        f[root] += f[lch[root]]
    if root < rch[root]:
        f[root] += f[rch[root]]
    ans = max(ans, f[root])
    return


if __name__ == '__main__':
    arr =[int(i) for i in input().split()]
    n = arr[0]
    root = arr[1]
    lch = [0 for i in range(10001)]
    rch = [0 for i in range(10001)]
    f = [1 for i in range(10001)]
    for i in range(n):
        arr = [int(j) for j in input().split()]
        lch[arr[0]] = arr[1]
        rch[arr[0]] = arr[2]
    dfs(root)
    print(ans)