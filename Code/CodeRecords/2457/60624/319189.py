def func11():
    n = int(input())
    happy = [0 for x in range(n+1)]
    for i in range(1,n+1):
        happy[i] = int(input())
    son = [[] for x in range(n+1)]
    vis = [False for x in range(n+1)]
    for i in range(1,n+1):
        temp = list(map(int, input().strip().split(" ")))
        son[temp[1]].append(temp[0])
        vis[temp[0]] = True
    root = 0
    for i in range(1,n+1):
        if not vis[i]:
            root = i
            break

    f = [[0,0] for x in range(n+1)]
    def treeDP(x:int):
        f[x][0] = 0
        f[x][1] = happy[x]

        for i in range(len(son[x])):
            y = son[x][i]
            treeDP(y)
            f[x][0] += max(f[y][0],f[y][1])
            f[x][1] += f[y][0]

    treeDP(root)
    res = max(f[root][0],f[root][1])
    print(res,end="")
    return
func11()