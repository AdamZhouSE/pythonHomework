from collections import defaultdict
n = int(input())
num = input().split(" ")
num = [int(i) for i in num]
num.insert(0, 0)
node = defaultdict(list)
v = defaultdict(int)
visited = [0] * (n + 1)
for i in range(n - 1):
    a_b = input().split(" ")
    a = int(a_b[0])
    b = int(a_b[1])
    node[a].append(b)
    node[b].append(a)


def dfs(x: int):
    v[x] += num[x]
    for i in range(len(node[x])):
        y = node[x][i]
        if not visited[y]:
            visited[y] = 1
            dfs(y)
            v[x] += max(0, v[y])
    return


visited[1] = 1
dfs(1)
print(max(v.values()))