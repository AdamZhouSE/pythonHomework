class left:
    def __init__(self, point):
        self.res = []
        self.point = point

def dfs(i):
    if f[i] != -1:
        return
    f[i] = node_list[i].point
    for j in range(len(node_list[i].res)):
        s = node_list[i].res[j]
        if vis[s] == 0:
            vis[s] = 1
            dfs(s)
            f[i] += max(0, f[s])

n = int(input())
a = list(input().strip().split(' '))
a = [int(x) for x in a]
vis = [0 for _ in range(n+2)]
f = [-1 for _ in range(n+2)]
node_list = [-1]
for i in range(n):
    node_list.append(left(a[i]))
for i in range(n-1):
    a = list(input().strip().split(' '))
    a = [int(x) for x in a]
    l = node_list[a[0]]
    r = node_list[a[1]]
    l.res.append(a[1])
    r.res.append(a[0])
vis[1] = 1
dfs(1)
print(max(f),end='')



