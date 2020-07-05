n = int(input())
graph = [[] for i in range(n)]
str1 = input()[2:-2]
pairs = []
if "],[" in str1:
    pairs = [[int(y) for y in x.split(",")] for x in str1.spilt("],[")]
else:
    pairs = [[int(y) for y in str1.split(",")]]
for pair in pairs:
    graph[pair[0]].append(pair[1])


def dfs(cur, k, visited):
    if cur in visited:
        return []
    if k == 1:
        return [[cur]]
    retv = []
    newvisited = visited.copy()
    newvisited.append(cur)
    for pc in graph[cur]:
        possible = dfs(pc, k - 1, newvisited)
        if len(possible) > 0:
            for p in possible:
                A = [cur]
                A.extend(p)
                retv.append(A)
    return retv

res = []
for x in range(n):
    res.extend(dfs(x, n, []))
print(res[0][::-1])