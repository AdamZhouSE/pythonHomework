n = eval(input())
longest = [0] * (n + 1)
secLongest = [0] * (n + 1)
res = [0]
graph = [[x] for x in range(0, n + 1)]


def dp(cur, pre):
    sz = len(graph[cur])
    for j in range(1, sz):
        if graph[cur][j] != pre:
            dp(graph[cur][j], cur)
            if longest[graph[cur][j]] + 1 > longest[cur]:
                secLongest[cur] = longest[cur]
                longest[cur] = longest[graph[cur][j]] + 1
            elif longest[graph[cur][j]] + 1 > secLongest[cur]:
                secLongest[cur] = longest[graph[cur][j]] + 1
    res[0] = max(res[0], longest[cur] + secLongest[cur])
    return


for i in range(0, n - 1):
    loc = [int(x) for x in input().split()]
    graph[loc[0]].append(loc[1])
    graph[loc[1]].append(loc[0])
dp(1, 1)
# print(graph)
print(res[0])